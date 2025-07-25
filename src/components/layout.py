from dash import Dash, html
import pandas as pd 
from . import bar_chart, year_dropdown, line_chart, country_checklist, area_graph, data_grid
import dash_bootstrap_components as dbc
from . import ids


def create_layout(app: Dash, data: dict[pd.DataFrame] ) -> html.Div:
    return html.Div(
        className="app-div",

        children=[
            html.Div(children=[
                html.H1(app.title),
                html.Hr(),
            ]),

            dbc.Stack([
                #Session I
                html.Div(children=[
        
                    #Session I - Title
                    html.H2(
                        className="section-title",
                        children=[
                            html.Div(ids.SESSION_I_TITLE)
                        ]),

                    #Session I - Filter
                    html.Div(
                        className="dropdown-container",
                        children=[year_dropdown.render(app, data["sales_data"], id="ev-trend")],
                        ),

                    #Session I - Graph
                    area_graph.render(app, 
                                      data=data["sales_data"], 
                                      id="ev-trend", 
                                      title="EV vs Non-EV Car Sales: Global Market Evolution (2010–2024)", 
                                      ylabel='Total car sales (millions)'),

                    #Session I - Comment
                    html.Div(ids.SESSION_I_COMMENT),

                    #Session I - Table
                    data_grid.render(app, 
                                     data=data["sales_data"], 
                                     id="ev-trend", 
                                     year_filter=True),

                ]),

                #Session II
                html.Div(children=[
                    #Session II - Title
                    html.H2(
                        className="section-title",
                        children=[
                            html.Div(ids.SESSION_II_TITLE)
                        ]),

                    #Session II - Filter
                    html.Div(
                        className="countries-container",
                        children=[
                            country_checklist.render(app, data["stock_share_data"], id="ev-share-stock")
                        ],),

                    #Session II - Graph
                    line_chart.render(app, 
                                      data["stock_share_data"], 
                                      id="ev-share-stock", 
                                      title="Share of cars currently in use that are electric, 2010 to 2024",
                                      ylabel="Share of car stocks that are electric (%)"
                        ),

                    html.Div(ids.SESSION_II_COMMENT),
                    
                    #Session II - Table
                    data_grid.render(app, 
                                     data=data["stock_share_data"], 
                                     id="ev-share-stock"),

                ]),
                
                #Session III
                html.Div(children=[
                    #Session III - Title
                    html.H2(
                        className="section-title",
                        children=[html.Div(ids.SESSION_III_TITLE)
                    ]),

                    #Session II - Filter
                    html.Div(
                        className="dropdown-container",
                        children=[year_dropdown.render(app, data["ev_phev_data"], id="ev-phev")]
                    ),

                    #Session II - Graph
                    bar_chart.render(app, 
                                     data=data["ev_phev_data"], 
                                     id="ev-phev", 
                                     title="Share of new cars sold that are battery-electric and plug-in hybrid, 2010 to 2024", 
                                     ylabel="Share of new cars sold (%)"),
                    
                    #Session II - Comment
                    html.Div(ids.SESSION_III_COMMENT),
                    
                    #Session II - Table
                    data_grid.render(app, 
                                     data=data["ev_phev_data"], 
                                     id="ev-phev",  
                                     year_filter=True),

                ]),
                
            ],
            gap=3,
        )]
    )