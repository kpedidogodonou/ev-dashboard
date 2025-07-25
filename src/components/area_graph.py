from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px 
import pandas as pd
from . import ids
from ..data.loader import DataSchema

MEDAL_DATA = px.data.medals_long()

def render(app: Dash, data: pd.DataFrame, id:str, title:str, ylabel:str) -> html.Div:
 
    @callback(
        Output(f"{ids.BAR_CHART}-{id}", "children"),
        Input(f"{ids.YEAR_DROPDOWN}-{id}", "value"),
        )
    def update_bar_chart(years: list[str]) -> html.Div:

        filtered_data = data.query("year in @years")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")

        fig = px.area(filtered_data, 
                      x=DataSchema.YEAR, 
                      y=DataSchema.SALES, 
                      color=DataSchema.CAR_TYPE, 
                      line_group="country",
                      title=title,
                      labels={"sales": ylabel, "year": "years"})


        return html.Div(dcc.Graph(figure=fig), id=f"{ids.BAR_CHART}-{id}")
    
    return html.Div(id=f"{ids.BAR_CHART}-{id}")
 