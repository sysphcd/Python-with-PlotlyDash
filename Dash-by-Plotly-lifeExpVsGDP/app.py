from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from pandas.io.formats import style
import plotly.express as px
import pandas as pd


app = Dash(__name__ ,external_stylesheets="https://codepen.io/chriddyp/pen/bWLwgP.css")

df = pd.read_csv("./life_expectancy.csv")
# print(df.info())
# min=df.Year.min()
# max=df.Year.max()
# print(min, " " , max)
colors = {"background": "#011833", "text": "#7FDBFF"}

app.layout = html.Div(
    [
        html.H1("My Dazzling Dashboard"),
        html.Div([html.Div(
                    [html.Label("Developing Status of the Country"),dcc.Dropdown(id="status-dropdown",
                                                                                options=[{"label": s, "value": s} for s in df.Status.unique()],
                                                                                className="dropdown",
                                                                                ),
                    ]),
                html.Div(
                    [html.Label("Average schooling years grater than"),dcc.Dropdown(id="schooling-dropdown",
                                                                                    options=[{"label": y, "value": y}
                                                                                                for y in range(
                                                                                                    int(df.Schooling.min()), int(df.Schooling.max()) + 1
                                                                                                )
                                                                                            ],
                                                                                    className="dropdown",
                                                                                    ),
                    ]),
                ],className="row",),
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),
        dcc.Slider(
            id="year-slider",
            min=df['Year'].min(),
            max=df['Year'].max(),
            step=None,
            marks={year: str(year) for year in range(df['Year'].min(), df['Year'].max() + 1)},
            value=df['Year'].min(),
        ),
    ],
    className="container",
)


@app.callback(
    Output("life-exp-vs-gdp", "figure"),
    Input("year-slider", "value"),
    Input("status-dropdown", "value"),
    Input("schooling-dropdown", "value"),
)
def update_figure(selected_year, country_status, schooling):
    filtered_dataset = df[(df.Year == selected_year)]

    if schooling:
        filtered_dataset = filtered_dataset[filtered_dataset.Schooling <= schooling]

    if country_status:
        filtered_dataset = filtered_dataset[filtered_dataset.Status == country_status]

    fig = px.scatter(
        filtered_dataset,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )

    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
