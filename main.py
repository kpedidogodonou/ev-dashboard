from dash import Dash
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from src.data.loader import load_sales_data, load_stock_share_data, load_ev_phev_data

def main() -> None: 
    data = {
        "sales_data": load_sales_data("https://ourworldindata.org/grapher/car-sales.csv?v=1&csvType=full&useColumnShortNames=true"),
        "stock_share_data": load_stock_share_data("https://ourworldindata.org/grapher/share-car-stocks-electric.csv?v=1&csvType=full&useColumnShortNames=true"),
        "ev_phev_data": load_ev_phev_data("https://ourworldindata.org/grapher/share-car-sales-battery-plugin.csv?v=1&csvType=full&useColumnShortNames=true")
    }
    app = Dash(external_stylesheets=[BOOTSTRAP, ""])
    app.title = "Global Trends in Electric Vehicle Adoption: A Data Analysis with Python"
    app.layout = create_layout(app, data)
    app.run(debug=True)

if __name__ == "__main__":
    main()
