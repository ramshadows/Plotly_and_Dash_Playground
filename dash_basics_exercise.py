import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html


import pandas as pd

app = dash.Dash()

#Read CSV File
old_faithful = pd.read_csv("Data1/OldFaithful.csv")

app.layout = html.Div([
    dcc.Graph(
        id = 'plotly_scatterplot',
        figure = {
            'data' : [go.Scatter(
                x= old_faithful['X'],
                y= old_faithful['Y'],
                mode= 'markers',
                marker = dict( size = 12, color = '#2d545e', symbol = 'circle',  line = {'width' : 0.5})
            )],

            'layout' : go.Layout(
                title = 'OldFaithful Town Eruption Duration  Vs Waiting Time Until The Next Eruption',
                xaxis = dict(title = 'Duration of Current Eruption (Minutes)'),
                yaxis = dict(title = 'Waiting Time Until Next Eruption (Minutes)'),
                hovermode = 'closest'
            )
        }
    )

])

if __name__ == '__main__':
    app.run_server()

