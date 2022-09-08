import json
import base64
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output

import pandas as pd


df = pd.read_csv("Data1/wheels.csv")

app = dash.Dash()

app.layout = html.Div([
    html.Div(
        dcc.Graph(
            id = "wheels-scatter-plot",
            figure = {
                "data" : [
                    go.Scatter(
                        x = df["color"],
                        y = df["wheels"],
                        dy = 1, #dy gives it a grid-like structure with a space of 1
                        mode = "markers",
                        marker = {"size" : 15},
                    ),
                ],

                "layout" : go.Layout(
                        title = "Capturing the Hover Data As Json",
                        hovermode = "closest",
                ),
            },
        ),
        style = {"width" : "30%", "float" : "left"}, #styles the html.div holding the dcc.graph
    ), 
    
  #Captures the json data as html preformated data
    html.Div(
        html.Pre(
        id = "selection",
        style = {"padding-top" : 35,}, #styling for html.pre
        ),
        style = {"width" : "30%"}, #styling for html.div
    ),


])

#Callback for hover data as a preformatted html
#For selection data just change the Id for the Input to selectedData
@app.callback(Output("selection", "children"), [Input("wheels-scatter-plot", "selectedData"),])
def json_data_callback(selectedData):
    return json.dumps(selectedData, indent=2)



if __name__ == '__main__':
    app.run_server(debug=True)