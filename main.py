#%%
import  pandas as pd

from data_utils import DataConnector
from data_extraction import DataExtractor

'''
def create_database(table_names, column, engine):
        column = 1
        database = pd.read_sql_table(table_names[column], engine)
        return database
'''

#extraction queries to obtain table names
dc = DataConnector()
de = DataExtractor()

name = "db_creds.yaml" 
credentials = dc.read_db_creds(name)
engine = dc.init_db_engine(credentials)
table_names = dc.list_db_tables(engine)
print(table_names)

column = 1
database = de.read_rds_table(table_names,column,engine)

database.head(3)