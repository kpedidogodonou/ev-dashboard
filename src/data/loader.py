import pandas as pd 

class DataSchema:
    COUNTRY_NAME = "country"
    COUNTRY_CODE = "country_code"
    YEAR = "year"
    CAR_TYPE = "car_type"
    SALES = "sales"
    EV_STOCK_SHARE = "ev_stock_share"

def load_sales_data(path: str) -> pd.DataFrame:
    # load the data from CSV file 
    data = pd.read_csv(
        path, storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'}
        )

    data = data.melt(id_vars=['Entity', 'Code', 'Year'], 
                    value_vars=['ev_sales', 'non_ev_cars_sold'],
                    var_name='car_type', value_name='sales')
    
    data.columns = ['country', 'country_code', 'year', "car_type", "sales"]

    data = data[data["country"] == "World"].sort_values(DataSchema.SALES, ascending=False)

  

    return data


def load_stock_share_data(path: str) -> pd.DataFrame:
      # load the data from CSV file 
    data = pd.read_csv(
        path, storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'}
        )
    data.columns = ['country', 'country_code', 'year', "ev_stock_share"]   
    return data


def load_ev_phev_data(path: str) -> pd.DataFrame:
      # load the data from CSV file 
    data = pd.read_csv(
        path, storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'}
        )
    

    data = data.melt(id_vars=['Entity', 'Code', 'Year'], 
                    value_vars=['phev_share_car_sales', 'bev_share_car_sales'],
                    var_name='car_type', value_name='sales')
    
    data.columns = ['country', 'country_code', 'year', "car_type", "sales"]

    data = data[data["country"] == "World"].sort_values(DataSchema.SALES, ascending=False)

    return data

