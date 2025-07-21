from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd
import requests
import plotly.express as px 
import dash_ag_grid as dag 
from src.components.layout import create_layout

from dash_bootstrap_components.themes import BOOTSTRAP

from src.data.loader import load_transaction_data

DATA_PATH = "https://ourworldindata.org/grapher/car-sales.csv?v=1&csvType=full&useColumnShortNames=true"


def main() -> None: 
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP, ""])
    app.title = "Global Trends in Electric Vehicle Adoption: A Data Analysis with Python"
    app.layout = create_layout(app, data)
    app.run(debug=True)

# Fetch the data.
df = pd.read_csv("https://ourworldindata.org/grapher/car-sales.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/car-sales.metadata.json?v=1&csvType=full&useColumnShortNames=true").json()

 

 


if __name__ == "__main__":
    main()


