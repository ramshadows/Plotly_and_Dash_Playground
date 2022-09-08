import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash()


app.layout = html.Div([
    dcc.Input(id = 'some_ref_id', value = 'SomeDefaultValue', type = 'text'),

    html.Div(
        id = 'another_ref_id',
    ),

])

@app.callback(Output(component_id = 'another_ref_id', component_property = 'children'),
[Input(component_id = 'some_ref_id', component_property = 'value')])
def update_div_output(output_value):
    return f"You entered: {output_value}"


if __name__ == '__main__':
    app.run_server()