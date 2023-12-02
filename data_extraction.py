#%%
import  psycopg2
import  pandas as pd
import  yaml

from data_utils import DataConnector as dc

from    sqlalchemy import create_engine
from    sqlalchemy import inspect
from    sqlalchemy import text



class DataExtractor:

    '''This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.'''

    def  __init__(self) -> None:
        pass

    ''' def read_rds_table(self):
        read = pd.read_sql_table(table_name, engine)
        return read'''

    def read_rds_table(self):
        df = pd.DataFrame([dict_result])
        return read


