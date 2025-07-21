import pandas as pd 

class DataSchema:
    COUNTRY_NAME = "country"
    COUNTRY_CODE = "country_code"
    YEAR = "year"
    CAR_TYPE = "car_type"
    SALES = "sales"



def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from CSV file 
    data = pd.read_csv(
        path,

    )


    data = data.melt(id_vars=['Entity', 'Code', 'Year'], 
                    value_vars=['ev_sales', 'non_ev_cars_sold'],
                    var_name='car_type', value_name='sales')
    data.columns = ['country', 'country_code', 'year', "car_type", "sales"]
    print(data.head())
    
    return data