#dcc.interval for live updating
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Output, Input

app = dash.Dash()


app.layout = html.Div([
    html.H1(
        id = "live-update-text",
    ),

    dcc.Interval(
        id = "interval-component",
        interval = 2000, #2 seconds
        n_intervals = 0,
    )

])

@app.callback(Output("live-update-text", "children"), [Input("interval-component", "n_intervals")])
def update_layout(n):
    return "Counter for number of Refreshes: {} ".format(n)


if __name__ == '__main__':
    app.run_server(debug=True)