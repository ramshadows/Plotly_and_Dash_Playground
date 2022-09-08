import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import numpy as np

np.random.seed(42)

app = dash.Dash()


#Create Data using numpy
random_x = np.random.randint(1, 101, 100)

random_y = np.random.randint(1, 101, 100)


app.layout = html.Div([
                        dcc.Graph(id = 'plotly_scatterplot',

                                  figure = {
                                             'data' : [go.Scatter(x= random_x,
                                                                  y= random_y,
                                                                  mode= 'markers',
                                                                  marker= {
                                                                            'size' : 12,
                                                                            'color' : '#2d545e',
                                                                            'symbol' : 'circle',
                                                                            'line' : {'width' : 2}

                                                                          })],
                                             'layout' : go.Layout(title="Plotly Scatter Plot Inside Dash",
                                                                   xaxis = {'title' : 'My X - Axis '})
                                           }



                                  ),

                        dcc.Graph(id = 'plotly_scatterplot_second_plot',

                                  figure = {
                                             'data' : [go.Scatter(x= random_x,
                                                                  y= random_y,
                                                                  mode= 'markers',
                                                                  marker= {
                                                                            'size' : 12,
                                                                            'color' : '#F7882F',
                                                                            'symbol' : 'pentagon',
                                                                            'line' : {'width' : 2}

                                                                          })],
                                             'layout' : go.Layout(title="Second Plotly Scatter Plot Inside Dash",
                                                                   xaxis = {'title' : 'My X - Axis '})
                                           }



                                  )

                        



                        ])

if __name__ == '__main__':
    app.run_server()