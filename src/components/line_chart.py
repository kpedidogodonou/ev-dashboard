from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px 
import pandas as pd
from . import ids
from ..data.loader import DataSchema
import plotly.io as pio
pio.templates.default = "plotly"

MEDAL_DATA = px.data.medals_long()

def render(app: Dash, data: pd.DataFrame, id, title, ylabel) -> html.Div:

    @callback(
        Output(f"{ids.LINE_CHART}-{id}", "children"),
        Input(f"{ids.COUNTRIES_CHECKLIST}-{id}", "value"),
        )
    def update_line_chart(countries: list[str]) -> html.Div:
        filtered_data = data.query("country in @countries")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")
        
        fig = px.line( 
            filtered_data,
            x=DataSchema.YEAR,
            y=DataSchema.EV_STOCK_SHARE,
            color=DataSchema.COUNTRY_NAME,
            markers=True,
            title=title,
            labels={'ev_stock_share':ylabel, 'year': 'years'},
            template="plotly",
        )
        return html.Div(dcc.Graph(figure=fig), id=f"{ids.LINE_CHART}-{id}")
    return html.Div(id=f"{ids.LINE_CHART}-{id}")




