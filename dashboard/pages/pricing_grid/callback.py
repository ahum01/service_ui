import dash
from dash import Output, Input, no_update, State
from dashboard.pages.pricing_grid.layout import layout

dash.register_page(module="pricing_grid", path="/", layout=layout())