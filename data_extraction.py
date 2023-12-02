import  psycopg2
import  panda as pd
import  yaml

from    sqlalchemy import create_engine
from    sqlalchemy import inspect
from    sqlalchemy import text



class DataExtractor:

    '''This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.'''

    def __init__(self) -> None:
        pass

    def read_rds_table (self, engine):
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM actor"))
            for row in result:
                print(row)