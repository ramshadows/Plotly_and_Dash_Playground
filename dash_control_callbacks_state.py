import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State



app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id = "value-in",
        #value = 1,
        style = {"font-size" : 24},
    ),

    html.Button(
        id = "submit-button",
        n_clicks = 0,
        children = "Submit",
        style = {"font-size" : 24}
    ),

    html.Div(
        id = "value-out",
    )


])

@app.callback(Output("value-out", "children"), [Input("submit-button", "n_clicks")], [State("value-in", "value")])
def callback_state_control(n_clicks, number):
    return f"{number} was entered. Submit button clicked {n_clicks} times"




if __name__ == '__main__':
    app.run_server(debug=True)