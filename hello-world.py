from dash import Dash, dcc  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="# Hello World - Let's build web apps in Python!")

# Customise your own layout
app.layout = dbc.Container([mytext])

# Run app
if __name__ == '__main__':
    app.run_server(port=8051)