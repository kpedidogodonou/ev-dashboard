import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame, id) -> html.Div:
    all_years: list[str] = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int)

    @app.callback(
        Output(f"{ids.YEAR_DROPDOWN}-{id}", "value"),
        Input(f"{ids.SELECT_ALL_YEARS_BUTTON}-{id}", "n_clicks"),
    )
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            #Title
            html.H6(
                className="badge bg-warning text-dark",
                children="Years"
            ),
            
            #Filter
            dcc.Dropdown(
                id=f"{ids.YEAR_DROPDOWN}-{id}",
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                multi=True,
            ),
            
            #Extra Button
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=f"{ids.SELECT_ALL_YEARS_BUTTON}-{id}",
                n_clicks=0,
            ),
        ]
    )