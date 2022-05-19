# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas
from dash import html

# pip3 freeze>requirements.txt  -> create requirements.txt

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df = pd.read_csv("social_capital.csv")
print(df.head())

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server # for deploy in Heroku
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Cesarean Delivery Rate',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
        dbc.Row(
            dbc.Col(html.Div("An automatically sized column"), width="auto")
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), width=3),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns"), width=3),
            ]
        ),
    ]
)
# app.layout = dbc.Container([dbc.Row([dbc.Col([mytitle], width=6)], justify='center'),
#                             dbc.Row([dbc.Col([mygraph], width=12)]),
#                             dbc.Row([dbc.Col([dropdown], width=6)], justify='center'),
# ], fluid=True)
app.layout = dbc.Container([dbc.Row([dbc.Col([mytitle], width=6)], justify='center'),
                            dbc.Row([dbc.Col([dropdown], width=3), dbc.Col([mygraph], width=9)])
                           
], fluid=True)

# Callback allows components to interact
@app.callback(
    Output(mygraph, 'figure'),
    Output(mytitle, 'children'),
    Input(dropdown, 'value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input

    print(column_name)
    print(type(column_name))
    # https://plotly.com/python/choropleth-maps/
    fig = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        color=column_name,
                        animation_frame='YEAR')

    return fig, '# '+column_name  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)