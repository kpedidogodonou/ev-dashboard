from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px 
import pandas as pd
from . import ids
from ..data.loader import DataSchema

MEDAL_DATA = px.data.medals_long()

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @callback(
        Output(ids.LINE_CHART, "children"),
        Input(ids.COUNTRIES_CHECKLIST, "value"),
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
            title="Share of cars currently in use that are electric, 2010 to 2024",
            labels={'ev_stock_share':'Share of car stocks that are electric', 'year': 'years'} 
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)
    return html.Div(id=ids.LINE_CHART)




