from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import requests

app = Dash()

app.layout = [
    html.H1(children='SONIA Curve Construction', style={'textAlign':'center'}, id='label_id'),
    # dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('label_id', 'value')
)
def update_graph(value):
    request_url = "http://127.0.0.1:8000/analytic_build_curve?curve_name=SONIA"
    x = requests.get(request_url)
    dff = pd.DataFrame.from_dict(x.json())
    dff['Date'] = pd.to_datetime(dff['pillar_dates'])
    return px.line(dff, x='Date', y='discount_factors')



if __name__ == '__main__':
    app.run()

