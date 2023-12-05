#%%
import  pandas as pd
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
            credentials = yaml.safe_load(stream)
            return credentials
                   
    def init_db_engine (self, credentials):
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        engine.connect()
        return engine
        
    def list_db_tables(self, engine):
        engine.connect()
        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, database, name, engine):
        database.to_sql(name, engine, if_exists='replace')


if __name__ == '__main__':
    pass

