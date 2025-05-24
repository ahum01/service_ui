import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html

def label_and_padding(label:str, font_size: str = "16px"):
    return dbc.Row(
        style={
            "margin":0,
            "padding":0,
        },
        children=[
            dbc.Label(label, style={"fontSize":font_size})
        ]
    )

def layout():
    page = dbc.Container(
        fluid=True,
        children=[
            dbc.Row(
                children=[
                    dbc.Col(children=[
                        html.Div([
                             label_and_padding("Dude")
                        ])
                    ])
                ]
            )
        ])
    return [page,dcc.Store(id='pricing_grid')]