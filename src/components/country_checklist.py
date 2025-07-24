import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_countries: list[str] = data["country"].tolist()
    unique_countries = sorted(set(all_countries))

 

    return html.Div(
        children=[
            html.H6("Year"),

            dcc.Checklist(
                id=ids.COUNTRIES_CHECKLIST,
                options=unique_countries,
                value=["Norway", "Germany", "Europe", "United States", "Sweden", "China", "World"],
                inline=True
                ),
        ]
    )