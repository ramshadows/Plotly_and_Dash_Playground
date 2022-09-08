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
    #html.Div(
        #html.Pre(
        #id = "hover-data",
        #style = {"padding-top" : 35,}, #styling for html.pre
       # ),
        #style = {"width" : "30%"}, #styling for html.div
   # ),

   #Captures the json data as a an html image
   html.Div([
        html.Img(
        id = "hover-image",
        src = "children", 
        height = 300,
                
       ),
        
   ], style = {"padding-top" : 115,},),




])
#Notice the Input parameter - Every dash core component has a "hoverData" component which has an id "hoverData"
#Callback for hover data as a preformatted html
#@app.callback(Output("hover-data", "children"), [Input("wheels-scatter-plot", "hoverData"),])
#def json_data_callback(hoverData):
    #return json.dumps(hoverData, indent=2)

#Callback for hover data as a Json image
@app.callback(Output("hover-image", "src"), [Input("wheels-scatter-plot", "hoverData"),])
def json_image_callback(hoverData):
    wheel = hoverData["points"][0]["y"]  #Grab the inner key of the hoverData  dictionary
    color = hoverData["points"][0]["x"]  #Grab the inner key of the hoverData  dictionary
    path = "Data1/Images/"

    return encode_image(path+df[(df["wheels"] == wheel) & (df["color"] == color)]['image'].values[0])

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())

    return  "data:image/png;base64,{}".format(encoded.decode())



if __name__ == '__main__':
    app.run_server(debug=True)