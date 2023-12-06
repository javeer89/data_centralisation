#%%
import  pandas as pd
import  tabula

from data_utils import DataConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from upload_dim_users import upload_to_dim_users


#extraction queries to obtain table names
dc              = DataConnector()
de              = DataExtractor()
dcl             = DataCleaning()
name            = "db_creds.yaml" 

credentials     = dc.read_db_creds(name)
engine          = dc.init_db_engine(credentials)
table_names     = dc.list_db_tables(engine)

#print(table_names) #testing.

column          = 1
database        = de.read_rds_table(table_names,column,engine)
#database is ready to be cleaned.

#database = dcl.clean_user_data(database)

#print(database.head())
#print("-------------------------------------")
#%%
#upload to dim_users

#%%

