from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px 
import pandas as pd
from . import ids
from ..data.loader import DataSchema

MEDAL_DATA = px.data.medals_long()

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.YEAR_DROPDOWN, "value"),
        )
    def update_bar_chart(years: list[str]) -> html.Div:
        filtered_data = data.query("year in @years")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")
        
        fig = px.bar(
           filtered_data,
            x=DataSchema.YEAR,
            y=DataSchema.SALES,
            color=DataSchema.CAR_TYPE,
            text_auto=True,
            title="EV vs Non-EV Car Sales: Global Market Evolution (2010–2024)",
            labels={'sales':'Total car sales (millions)', 'year': 'years'} 
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)
 


