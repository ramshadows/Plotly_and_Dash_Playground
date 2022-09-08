import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash.dependencies import Input, Output, State
from pandas_datareader import data, wb
from datetime import datetime

app = dash.Dash()

nsdq = pd.read_csv("Data1/NASDAQcompanylist.csv")

nsdq.set_index("Symbol", inplace = True)
options = []

for symbol in nsdq.index:
    #{"label" : "What user sees", "value" : "What scripts sees "}
    mydict = {}

    mydict["label"] = nsdq.loc[symbol]["Name"] + " " + symbol #Apple Co. AAPL
    mydict["value"] = symbol
    options.append(mydict)

app.layout = html.Div([

    html.H1("Stock Ticker Dashboard"),

    html.Div([
        html.H3("Enter a Stock Symbol", style = {"padding-right" : "30px"}),
    dcc.Dropdown(
        id = "my-stock-picker",
        options = options,
        value = ["TSLA"], #Set as default value
        multi = True,
        
    ),

    ], style = {"display" : "inline-block", "verticla-align" : "top", "width" : "30%"}),

    html.Div([
        html.H3("Select a Start and End Date", style = {"padding-right" : "30px"}),
        dcc.DatePickerRange(
            id = "my-date-picker",
            min_date_allowed = datetime(2015, 1, 1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today(),
         ),


    ], style = {"display" : "inline-block", "vertical-align" : "top"}),

    html.Div([
        html.Button(
            id = "submit-button",
            n_clicks = 0,
            children = "Submit",
            style = {"font-size" : 24, "margin-left" : "30px"}
        )
    ], style = { "display" : "inline-block", "vertical-align" : "bottom"}),
    
    dcc.Graph(
        id = "my-stock-graph",
        figure = {
            "data" : [
                {
                    "x" : [1, 2],
                    "y" : [3, 1],
                }
            ],
        }
    ),

])


@app.callback(Output("my-stock-graph", "figure"),
              [Input("submit-button", "n_clicks")],
             [State("my-stock-picker", "value"),
              State("my-date-picker", "start_date"),
              State("my-date-picker", "end_date")])
def update_graph(n_cliks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")

    #Grab the stock name from the list
    traces = []

    for stock in stock_ticker:
        #Grab the data from the web using pandas datareader
        df = data.DataReader(stock, "yahoo", start, end)
        traces.append(
            {
                "x" : df.index,
                "y" : df["Close"],
                "name" : stock,
            }

        )

    fig = {
        "data" : traces,
        "layout" : {"title" : stock_ticker}
    }

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
