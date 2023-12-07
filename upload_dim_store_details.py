#connected file imports
from data_utils import DataConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning



def upload_to_dim_store_details():
        #import class variables
        dc              = DataConnector()
        de              = DataExtractor()
        dcl             = DataCleaning()
        #source data
 
        sql_name        = "dim_store_details"
        #connect and create database
        database        = de.retrieve_store_data

        #clean database
        #card_details = dcl.clean_card_details(card_details)
        #cleanig code is mashing up the upload. figure it out later.

        #connect to local server
        local_name      = "db_creds_local.yaml" 
        credentials     = dc.read_db_creds(local_name)
        engine          = dc.init_db_engine(credentials)
        
        #UPLOAD
        dc.upload_to_db(database, sql_name, engine)

upload_to_dim_store_details()