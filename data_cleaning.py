#%%
import  psycopg2
import  pandas          as pd
import  yaml

from data_utils         import DataConnector as dc
from data_extraction    import DataExtractor as dx

from    sqlalchemy      import create_engine
from    sqlalchemy      import inspect
from    sqlalchemy      import text

class DataCleaning:
    '''clean data from each of the data sources'''

    def __init__(self) -> None:
        pass

    def clean_user_data(self,df):
        df = self.clean_invalid_date(df,'date_of_birth')
        df = self.clean_invalid_date(df,'join_date')        
        df = self.clean_NaNs_Nulls_misses(df)
        df.drop(columns='1',inplace=True)
        return df


