import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output

import numpy as np
import pandas as pd



app = dash.Dash()


#READ DATA
df = pd.read_csv("Data1/mpg.csv")

#ADDING SOME JITTER
#EXAMPLE - 1978 + (-0.3 * 0.1) = 1977.7
df["year"] = np.random.randint(-4, 5, len(df)) * 0.1 + df["model_year"]

app.layout = html.Div([

    html.Div([

        dcc.Graph(
        id = "mpg-scatter",
        figure = {
            "data" : [
                go.Scatter(
                    x = df["year"] + 1900,
                    y = df["mpg"],
                    mode = "markers",
                    text= df["name"],
                    hoverinfo= "text + y + x",
                )
            ],
            "layout" : go.Layout(
                title= "MPG Data",
                xaxis= dict(title= "Model Year",),
                yaxis= dict(title= "MPG"),
                hovermode= "closest"
            )
        }
    )
    ], style = {"width" : "50%", "display" : "inline-block"}),


    html.Div([

        dcc.Graph(
        id = "mpg-line",
        figure = {
            "data" : [
                go.Scatter(
                    x = [0, 1],
                    y = [0, 1],
                    mode = "lines",
                )
            ],
            "layout" : go.Layout(
                title= "Acceleration",
                margin= dict(l= 0),
            )
        }
    )
    ], style = {"width" : "20%", "height" : "50%", "display" : "inline-block"}),

    html.Div([
        dcc.Markdown(
            id = "mpg-stats",

        )
    ], style = {"width" : "20%", "height" : "50%", "display" : "inline-block"}),

    
])


@app.callback(Output("mpg-line", "figure"), [Input("mpg-scatter", "hoverData")])
def callback_graph(hoverData):
    vehicle_index = hoverData['points'][0]['pointIndex']

    figure = {
        "data" : [
            go.Scatter(
                x= [0, 1],
                y= [0, 60/df.iloc[vehicle_index]['acceleration']], # 0 - 60 miles per hour
                mode= "lines",
                line = dict(width = 2 * df.iloc[vehicle_index]["cylinders"]), #set the thickness of the line by 2 * number of cylinders

            )
        ],
        "layout" : go.Layout(
            title= df.iloc[vehicle_index]['name'],
            xaxis= dict(visible = False),
            yaxis= dict(visible = False, range = [0, 60/df["acceleration"].min()]),
            margin= dict(l = 0),
            height= 300,
        )
    }

    return figure

@app.callback(Output("mpg-stats", "children"), [Input("mpg-scatter", "hoverData")])
def callback_stats(hoverData):
    vehicle_index = hoverData['points'][0]['pointIndex']

    stats = """

            {} Cylinders \n
            {}cc Displacement \n
            0 to 60 mph in {} seconds

            """.format(df.iloc[vehicle_index]["cylinders"],
                       df.iloc[vehicle_index]["displacement"],
                       df.iloc[vehicle_index]["acceleration"],
                       )

    return stats






if __name__ == '__main__':
    app.run_server(debug=True)
