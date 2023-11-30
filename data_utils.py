#%%
import  psycopg2
import  panda as pd
import  yaml

from    sqlalchemy import create_engine
from    sqlalchemy import inspect

#CLASS Data Connector
class   DataConnector:
    '''connect with and upload data to the database'''

    def __init__(self) -> None:
        pass

    def read_db_creds(self, name):
        with open(name, 'r') as stream:
            return yaml.safe_load(stream)
    
    def init_db_engine (self, credentials):
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")     
        return engine
    
    def list_db_tables(self, engine):
        inspector = inspect(engine)
        return inspector.get_table_names()



#%%

import  yaml
def read_db_creds(name):
    with open(name, 'r') as stream:
        return yaml.safe_load(stream)

db = "db_creds.yaml"
read_db_creds(db)

#progress notes: so we will need a way to define "name" object later on in code.

#%%

import psycopg2
with psycopg2.connect(host='data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com', user='aicore_admin', password='AiCore2022', dbname='postgres', port=5432) as conn:
    with conn.cursor() as cur:
        cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
        for table in cur.fetchall():
            print(table)

#used psycopg2 to view table for any needed information. none needed as of yet.

#%%
import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd

def read_db_creds(name):
    with open(name, 'r') as stream:
        return yaml.safe_load(stream)

db = "db_creds.yaml"
credentials = read_db_creds(db)
rdbkey = read_db_creds(db).keys()
rdbvalues = read_db_creds(db).values()

print(list(rdbkey)[2])
print(list(rdbvalues)[1])

#engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")     

inspector = inspect(engine)
inspector.get_table_names()