#%%
import  psycopg2
import  pandas as pd
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
    name = "db_creds.yaml" #need to make dynamic
    dc = DataConnector()
    credentials = dc.read_db_creds(name)
    engine = dc.init_db_engine(credentials)
    engine.connect()
    #print(engine) #can remove
    dbt = dc.list_db_tables(engine)
    #print(dbt) #can remove
    with engine.connect() as connection: #need to make dyanimc like sourcing from dbt[1] instead of named column
        result = pd.read_sql_table(dbt[1], engine)
        dict_result = dict(result.head(3))
        #print(dict_result)
        #print(type(dict_result))
        #print(result.head(10))
        #print(type(result))
        #print(result.head(10))

    df = pd.DataFrame([dict_result])
    print(type(df))
df.head(10)


    