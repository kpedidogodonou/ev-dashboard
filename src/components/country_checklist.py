import pandas as pd
from dash import Dash, dcc, html

from . import ids


def render(app: Dash, data: pd.DataFrame, id:str) -> html.Div:
    all_countries: list[str] = data["country"].tolist()
    unique_countries = sorted(set(all_countries))

 

    return html.Div(
        className="card-body bg-warning mb-3 rounded p-3",
        children=[
            # Title
            html.H6(
                className="badge bg-warning text-dark",
                children="Countries"
            ),

            #Checklist
            dcc.Checklist(
                id=f"{ids.COUNTRIES_CHECKLIST}-{id}",
                options=unique_countries,
                value=["Norway", "Germany", "Europe", "United States", "Sweden", "China", "World"],
                inline=True
            ),
        ]
    )