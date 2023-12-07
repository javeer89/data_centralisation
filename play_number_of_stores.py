#%%
import requests
import json
import pandas as pd

def API_key():
        return {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}  
    
def API_url_number_stores():
        return "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
    
def list_number_of_stores():
        # Send a GET request to obtain information about number of stores
        response =  requests.get(url = API_url_number_stores(), headers = API_key() )
        data = response.json()['number_stores']        
        return data
        


def retrieve_store_data():
        store_data = [] #creating list
        number_of_stores = list_number_of_stores()

        for store_number in range(number_of_stores):
                response = requests.get(url = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}",
                                        headers = API_key() )
                data = pd.json_normalize(response.json())
                store_data.append(data)
        
        return pd.concat(store_data)


retrieve_store_data()
