#connected 
import  pandas as pd
import  yaml

#connected file imports
from data_utils import DataConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning



def upload_to_dim_users():
        #import class variables
        dc              = DataConnector()
        de              = DataExtractor()
        dcl             = DataCleaning()
        #source data
        name            = "db_creds.yaml" 

        #connect and create table
        credentials     = dc.read_db_creds(name)
        engine          = dc.init_db_engine(credentials)
        table_names     = dc.list_db_tables(engine)
        column          = 1 #user_data
        database        = de.read_rds_table(table_names,column,engine)

        #clean database
        database = dcl.clean_user_data(database)

        #connect to local server
        local_name      = "db_creds_local.yaml" 
        credentials     = dc.read_db_creds(local_name)
        engine          = dc.init_db_engine(credentials)
        
        #UPLOAD
        dc.upload_to_db(database,'dim_users',engine)

upload_to_dim_users()