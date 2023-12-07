#%%
import  pandas as pd
import  tabula
import  boto3
import  requests
import  json

from    data_utils import DataConnector


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


    #STORE DATA
    '''API Variables as Methods'''
    def API_key(self):
        return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}  
    
    def API_url_number_stores(self):
            return "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
        
    '''Evaluate number of stores'''
    def list_number_of_stores(self):
            response =  requests.get(url = self.API_url_number_stores(), headers = self.API_key())
            data = response.json()['number_stores']        
            return data

    '''GET Store Data'''
    def retrieve_store_data(self):
            store_data = [] #creating list
            number_of_stores = self.list_number_of_stores()
            
            #iterate through each store number and compile details into database
            for store_number in range(number_of_stores):
                    response = requests.get(url = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}",
                                            headers = self.API_key() )
                    data = pd.json_normalize(response.json())
                    store_data.append(data)
            
            return pd.concat(store_data)



if __name__ == '__main__':
    

    pass

