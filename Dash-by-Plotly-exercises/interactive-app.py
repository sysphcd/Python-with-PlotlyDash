from dash import Dash, dcc, Output, Input 
import dash_bootstrap_components as dbc 

# Build your componets : SOLAR is dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

mytext = dcc.Markdown(children='')
myinput = dcc.Input(value="# Hello World - Let's build web app in Python!")

# Customise your own layout
app.layout = dbc.Container([mytext, myinput])

# Callback allows components to interact :  links example : [this link](https://google.com)
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)

def update_title(user_input): # function arguments come from the components property of the Input
    return user_input # returned objects are assigned to the components property of the Output

if __name__ == '__main__':
    app.run_server(port=8051)    
