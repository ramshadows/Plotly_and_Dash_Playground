import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output

import pandas as pd

mpg = pd.read_csv("Data1/mpg.csv")

app = dash.Dash()

#List of mpg df columns
features = mpg.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id = "xaxis-dropdown",
            options = [{ "label" : i, "value" : i} for i in features],
            value = "displacement",
        ),
    ], style = {'width' : '15%', 'display' : 'inline-block', 'padding' : '10px 15px',
     'box-sizing' : 'border-box', 'box-shadow': '0 1px 5px rgba(0, 0, 0, 0.5)', 'position' : 'relative' }),

    html.Div([
        dcc.Dropdown(
            id = "yaxis-dropdown",
            options = [{ "label" : i, "value" : i} for i in features],
            value = "mpg",

        ),
    ], style = {'width' : '15%', 'display' : 'inline-block',  'padding' : '10px 15px', 'vertical-align': 'right',
    'box-sizing' : 'border-box', 'box-shadow': '0 1px 5px rgba(0, 0, 0, 0.5)', 'position' : 'relative'}),

    dcc.Graph(
        id = "multi-callbacks-graph"
    )



])


@app.callback(Output("multi-callbacks-graph", "figure"), [Input("xaxis-dropdown", "value"),
Input("yaxis-dropdown", "value")])
def update_graph(xaxis_value, yaxis_value):
    return {
        "data" : [go.Scatter(
            x = mpg[xaxis_value],
            y = mpg[yaxis_value],
            text = mpg["name"],
            mode = "markers",
            marker = dict( size = 12, symbol = 'circle',  line = {'width' : 2}), 
        )],
        "layout" : go.Layout(
                title = 'MPG DATA COMPARISON',
                xaxis = dict(title = xaxis_value, type = 'log'),
                yaxis = dict(title = yaxis_value),
                hovermode = 'closest'
            ),
    }


if __name__ == '__main__':
    app.run_server(debug=True)