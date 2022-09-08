import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output



app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(
        id = "range-slider",
        min = 0,
        max = 100,
        marks = {i : str(i) for i in range(0, 101, 5)},
        value = [0, 100]
    ),

    html.Div(
        id = "product",
    ),



])

@app.callback(Output("product", "children"), [Input("range-slider", "value")])
def slider_callback(value_list):
    return value_list[0] * value_list[1]




if __name__ == '__main__':
    app.run_server(debug=True)