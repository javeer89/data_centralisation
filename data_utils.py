#%%
import  psycopg2
import  panda as pd
import  yaml

from    sqlalchemy import create_engine
from    sqlalchemy import inspect
from    sqlalchemy import text

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


if __name__ == '__main__':
    dc = DataConnector()
    engine = dc.init_db_engine()
    engine.connect()
    print("Hi") 
    print(engine)
    dbt = dc.list_db_tables(engine)
    print(dbt)
    with engine.connect() as connection:
        result = connection.execute(text())
        for row in result:
            print(row)
            