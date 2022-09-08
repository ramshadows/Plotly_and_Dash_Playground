import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

#Styling html components
colors = {'background' : '#e8f9fd', 'text' : '#7d3cff'}


app.layout = html.Div(children = [
    html.H1("Dash: Web Dashboard with Python", style={'textAlign' : 'center',
                                                       'color' : colors['text']                                                 
                                                    }),
    
    dcc.Graph(id='first_graph',
               figure = {'data' : [{'x': [1, 2, 3], 
                                    'y' : [4, 2, 1],
                                    'type' : 'bar',
                                    'name' : 'San Francisco'
                                    },

                                    {'x': [1, 2, 3], 
                                    'y' : [2, 4, 5],
                                    'type' : 'bar',
                                    'name' : 'New York'
                                    },
                                    
                                    
                                    
                                    ],

                          'layout' : {

                                     'title' : 'Bar Plots' ,
                                     'plots_bgcolor' : colors['background'],
                                     'paper_bgcolor' : colors['background'],
                                     'font' : {'color' : colors['text']}
                                     }
                        
                        }
               
    ),
], style={'backgroundColor' : colors['background']}

)


if __name__ == '__main__':
    app.run_server()
