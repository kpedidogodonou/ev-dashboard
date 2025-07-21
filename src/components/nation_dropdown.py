from dash import Dash, html, dcc, callback, Input, Output
from . import ids


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "Canada", "China"]

    @callback(
        Output(component_id=ids.NATION_DROPDOWN, component_property="value"),
        Input(component_id=ids.SELECT_ALL_NATIONS_BUTTON, component_property="n_clicks"))
    def select_all_nations(_: int) -> list[str]:
        return all_nations



    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                options =[{"label": nation, "value": nation} for nation in all_nations ],
                value=all_nations,
                multi=True
            ),
            html.Button(
                id=ids.SELECT_ALL_NATIONS_BUTTON,
                className="dropdown-button",
                children=["Select All"]
            )
        ]
    )