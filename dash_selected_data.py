import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output

import numpy as np
import pandas as pd


app = dash.Dash()

#CREATE DATA
np.random.seed(10)


x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

#CREATE THE DATAFRAMES
df1 = pd.DataFrame({"X" : x1, "Y" : y}) #Note the X and Y will be our columns
df2 = pd.DataFrame({"X" : x1, "Y" : y}) #Note the X and Y will be our columns #Duplicate
df3 = pd.DataFrame({"X" : x2, "Y" : y}) #Note the X and Y will be our columns

#MERGE THE DFS
df = pd.concat([df1, df2, df3])


#CREATING OUR LAYOUT
app.layout = html.Div([

    html.Div([


        dcc.Graph(
        id = "plot",
        figure = {
            "data" : [
                go.Scatter(
                    x = df["X"],
                    y = df["Y"],
                    mode = "markers",
                )
            ],
            "layout" : go.Layout(
                title= "Scatter Plot",
                hovermode= "closest",
            )
        }
    ),

        
    ], style = {"width" : "30%", "display" : "inline-block"}),


    html.Div([

        html.H1(
            id = "density",
            style = {"padding-top" : 25},
        ),

    ], style = {"width" : "30%", "display" : "inline-block", "vertical-align" : "top"}),
    




])


#CREATE THE CALLBACK


@app.callback(Output("density", "children"), [Input("plot", "selectedData")])
def find_density(selectedData):
    """ Calculate the density """
    pts = len(selectedData["points"])
    range_or_lassopoints = list(selectedData.keys())
    range_or_lassopoints.remove("points")
    max_x = max(selectedData[range_or_lassopoints[0]]["x"])
    min_x = min(selectedData[range_or_lassopoints[0]]["x"])
    max_y = max(selectedData[range_or_lassopoints[0]]["y"])
    min_y = min(selectedData[range_or_lassopoints[0]]["y"])


    area = (max_x - min_x) * (max_y - min_y)
    dense = pts/area

    return "Density = {:.2f}".format(dense)



if __name__ == '__main__':
    app.run_server(debug=True)
