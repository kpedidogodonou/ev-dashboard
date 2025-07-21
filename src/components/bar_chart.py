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
        
        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.SALES,
                index=[DataSchema.YEAR, DataSchema.CAR_TYPE],
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(DataSchema.SALES, ascending=False)
        
        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.YEAR,
            y=DataSchema.SALES,
            color=DataSchema.CAR_TYPE,
            text_auto=True,
            title="EV vs Non-EV Car Sales: Global Market Evolution (2010–2024)",
            labels={'sales':'Total car sales (millions)', 'year': 'years'} 
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)

""" def render(app: Dash) -> html.Div: 

    @callback(
        Output(component_id=ids.BAR_CHART, component_property="children"),
        Input(component_id=ids.NATION_DROPDOWN, component_property="value"))
    def update_bar_chart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @nations")

        if filtered_data.shape[0] == 0:
            return html.Div("No Data Selected")

        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(
            dcc.Graph(figure=fig)    
        )
    
    return html.Div(id=ids.BAR_CHART) """


