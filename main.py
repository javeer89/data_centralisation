'''
    main python script page will be developed
    AFTER I have completed all stages of the work.

    I've had too much trouble being setback on how to run things that for now operating via independant files
    have been more fortuitous for me and allowed me to make progress.

    EVERYTHING written below is just jargon and notes for my work.
'''
#%%
import  pandas as pd
import  tabula
import requests

from data_utils import DataConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from upload_dim_users import upload_to_dim_users




#GIT generated token via developer settings.
MY_GENERATED_TOKEN =    "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"

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




