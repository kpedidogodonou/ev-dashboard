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
                        children=[year_dropdown.render(app, data["sales_data"], id="ev-trend")],),
                        bar_chart.render(app, data["sales_data"], id="ev-trend", title="EV vs Non-EV Car Sales: Global Market Evolution (2010–2024)", ylabel='Total car sales (millions)'),
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
                
                html.Div(children=[
                    html.H2("3. Electric Shift: Battery vs Plug-In Hybrid Sales Trends"),
                    html.Div(
                        className="dropdown-container",
                        children=[year_dropdown.render(app, data["ev_phev_data"], id="ev-phev")]),
                        bar_chart.render(app, data["ev_phev_data"], id="ev-phev", title="Share of new cars sold that are battery-electric and plug-in hybrid, 2010 to 2024", ylabel="Share of new cars sold (%)"),
                        html.Div("This graph shows the global share of new car sales that are electric, broken down into battery-electric vehicles (BEVs) and plug-in hybrid electric vehicles (PHEVs), from 2010 to 2024. The data reveals that BEVs (in blue) consistently account for the majority of electric car sales, with their market share increasing sharply after 2020. PHEVs (in red) also grew, but at a slower pace, indicating a global shift in consumer preference toward fully electric vehicles. By 2024, BEVs made up nearly 14% of all new cars sold, compared to just over 8% for PHEVs—highlighting the accelerating transition away from hybrid solutions toward fully electric mobility.")
                ]),
                
            ],
            gap=3,
        )
                 
        ]
    )