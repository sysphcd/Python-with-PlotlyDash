from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# incorporate data into app
df = px.data.medals_long()

# Build your componets : SOLAR is dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytext = dcc.Markdown(children='# App that analyzes Olympic mdeals')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # initial value displayed when page first loads
                        clearable=False
)

# Cusomise your layout
app.layout = dbc.Container([mytext, mygraph, dropdown])

# Callback  allows components to interact :  links example : [this link](https://google.com)
@app.callback(
    Output(mygraph, component_property = 'figure'),
    Input(dropdown, component_property='value')
)

def update_graph(user_input) :  # function arguments come from the component property of the Input
    if user_input == 'Bar Plot' :
        fig = px.bar(data_frame=df, x="nation", y="count", color="medal")
    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="nation", y="count", color="medal", symbol="medal")
    
    return fig  # returned objects are assigned to the component property of the Output

if __name__ == '__main__':
    app.run_server(port=8051)
