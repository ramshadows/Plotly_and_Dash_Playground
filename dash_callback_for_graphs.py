import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from dash.dependencies import Input, Output

import pandas as pd


gdp_data = pd.read_csv("Data1/gapminderDataFiveYear.csv")


app = dash.Dash()

year_options = []

for year in gdp_data['year'].unique():
    year_options.append({'label' : str(year), 'value' : year})


app.layout = html.Div([
    dcc.Graph(id = 'gdp-graph'),
    dcc.Dropdown(id = 'year-picker', options = year_options, value = gdp_data['year'].min())




])

@app.callback(Output(component_id='gdp-graph', component_property='figure'),
[Input(component_id='year-picker', component_property='value')])
def update_figure(selected_year):

    #Filter gdp_data by year selected
    filtered_by_year_df = gdp_data[gdp_data['year'] == selected_year]

    traces = []


    for continent_name in filtered_by_year_df['continent'].unique():
        #Filter seleted year df now by continent
        df_by_continent = filtered_by_year_df[filtered_by_year_df['continent'] == continent_name]

        traces.append(go.Scatter(
            x = df_by_continent['gdpPercap'],
            y = df_by_continent['lifeExp'],
            mode ='markers',
            text = df_by_continent['country'],
            marker = dict( size = 12, symbol = 'circle',  line = {'width' : 2}),
            name = continent_name,
            opacity = 0.7,

        ))

    return {'data' : traces, 'layout' : go.Layout(
                title = 'GDP Per Capita Vs Life Expectancy ',
                xaxis = dict(title = 'GDP Per Capita', type = 'log'),
                yaxis = dict(title = 'Life Expectancy'),
                hovermode = 'closest'
            )}



if __name__ == '__main__':
    app.run_server(debug=True)