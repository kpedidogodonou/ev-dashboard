from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px 
import pandas as pd
from . import ids
import dash_ag_grid as dag
MEDAL_DATA = px.data.medals_long()

def render(app: Dash, data: pd.DataFrame, id:str, year_filter:bool=False) -> html.Div:

 
    @callback(
        Output(f"{ids.DATA_GRID}-{id}", "children"),
        Input(f"{ids.YEAR_DROPDOWN}-{id}" if year_filter else f"{ids.COUNTRIES_CHECKLIST}-{id}", "value"),
        )
    def update_bar_chart(years: list[str]) -> html.Div:
        
        filtered_data = data.query("year in @years") if year_filter else data
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")


        grid = dag.AgGrid(
            rowData=filtered_data.to_dict("records"),
            columnDefs=[{"field": i} for i in filtered_data.columns],
            dashGridOptions={'pagination':True, "paginationPageSize": 10, "paginationAutoPageSize": True },
        )
    

        return html.Div(
            children=[
                grid,
                html.Div("Data sources: International Energy Agency. Global EV Outlook 2025. – processed by Our World in Data")
            ],
            id=f"{ids.DATA_GRID}-{id}"
            )
    
    return html.Div(id=f"{ids.DATA_GRID}-{id}")
 


