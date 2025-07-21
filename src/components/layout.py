from dash import Dash, html
import pandas as pd 
from . import nation_dropdown, bar_chart, year_dropdown
import dash_bootstrap_components as dbc



def create_layout(app: Dash, data: pd.DataFrame ) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
             dbc.Stack(
            [
                html.Div(children=[
                    html.H1(app.title),
                    html.Hr(),
                ]),

                html.Div(children=[
                      html.H2("1. Are EVs Replacing Conventional Cars?"),
                        html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data)
                    ],
            ),
            bar_chart.render(app, data),
                    html.Div("This chart illustrates the global sales of electric vehicles (EVs) compared to non-electric cars from 2010 to 2024. While non-EV sales have remained relatively stable, the share of EVs has increased significantly—especially after 2020. This shift highlights the accelerating transition toward cleaner mobility, driven by technological improvements, policy incentives, and growing consumer demand for sustainable transport solutions.")

                ]),

                
            ],
            gap=3,
        )
            
          
        ]
    )