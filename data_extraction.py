#%%
import  pandas as pd
import  tabula

from data_utils import DataConnector


'''
from    sqlalchemy import create_engine
from    sqlalchemy import inspect
from    sqlalchemy import text
'''

class DataExtractor:

    def  __init__(self) -> None:
        pass
    
    #read database 
    def read_rds_table(self, table_names, column, engine):
        column = 1
        database = pd.read_sql_table(table_names[column], engine)
        return database
    
    #retreive card details
    def retreive_pdf_data (self, link):
        return pd.concat(tabula.read_pdf(link, pages='all'))
        

if __name__ == '__main__':
    

    pass

