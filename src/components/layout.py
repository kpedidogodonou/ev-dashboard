from dash import Dash, html
import pandas as pd 
from . import bar_chart, year_dropdown, line_chart, country_checklist
import dash_bootstrap_components as dbc


def create_layout(app: Dash, data: dict[pd.DataFrame] ) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.Div(children=[
                html.H1(app.title),
                html.Hr(),]),

            dbc.Stack([
                html.Div(children=[
                    html.H2("1. Are EVs Replacing Conventional Cars?"),
                    html.Div(
                        className="dropdown-container",
                        children=[year_dropdown.render(app, data["sales_data"])],),
                        bar_chart.render(app, data["sales_data"]),
                        html.Div("This chart illustrates the global sales of electric vehicles (EVs) compared to non-electric cars from 2010 to 2024. While non-EV sales have remained relatively stable, the share of EVs has increased significantly—especially after 2020. This shift highlights the accelerating transition toward cleaner mobility, driven by technological improvements, policy incentives, and growing consumer demand for sustainable transport solutions.")
                ]),
                
                html.Div(children=[
                    html.H2("2. Global EV Penetration: Who’s Leading on the Road?"),
                    html.Div(
                        className="dropdown-container",
                        children=[
                            country_checklist.render(app, data["stock_share_data"])
                            ],),
                    line_chart.render(app, data["stock_share_data"]),
                    html.Div("This graph shows the share of cars currently in use that are electric across selected countries from 2010 to 2024. Norway stands out as the global leader, reaching over 30% electric vehicle (EV) penetration in its national fleet — a result of strong government incentives, infrastructure investments, and early policy adoption. Sweden and China also show consistent growth, with China surpassing 10% by 2024. In contrast, regions like the United States and Germany are progressing more slowly, reflecting differences in policy support and consumer adoption. The world average remains below 5%, highlighting that despite growing EV sales, the global vehicle fleet is still largely composed of internal combustion engine cars.")
                ]),
            ],
            gap=3,
        )
                 
        ]
    )