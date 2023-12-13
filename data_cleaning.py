#%%
import  pandas          as pd
import  numpy           as np
#import  phonenumbers

#data cleaning tools
class   DataCleaning:

            def __init__(self) -> None:
                pass
            '''  
            def drop_index(self, database):
                database = database.drop(columns = "index")

            #adjust dates to format into correct form
            def clean_date(self, database, column_name):
                database[column_name] = pd.to_datetime(database[column_name], errors='ignore', format= '%Y %b %d')

            #clean phone numbers and make them into a standardised format    
            def clean_phone_numbers(self, database, column_name):
                database[column_name]

            def clean_country_code(self, database, column_name):
                database[column_name]
        
            '''
            #T3
            #CLEAN USER
            def clean_user_data(self,database):
                    database                        = database.drop(columns="index")
                    database["date_of_birth"]       = pd.to_datetime(database["date_of_birth"], "coerce", format = "%Y-%m-%d")
                    database["join_date"]           = pd.to_datetime(database["join_date"], "coerce", format = "%Y-%m-%d")

                    return database

            #T4
            #CLEAN CARD DETAILS
            def clean_card_details(self, database):

                    return database
            
            #T5
            #CLEAN STORE DETAILS
            def clean_store_data (self, database):
                
                return database

            #T6
            #CLEAN PRODUCTS DATA
            def clean_products_data (self, database):
                
                return database

            #T7
            #CLEAN ORDERS DATA
            def clean_orders_data (self, database):
                    database = database.drop(columns= ["level_0", "index", "1"] )
                    database = database.dropna()

                    return database

            #T8
            #CLEAN EVENT DATES
            def clean_event_dates (self, database):
                    database["month"]       = pd.to_numeric(database["month"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["year"]        = pd.to_numeric(database["year"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["day"]         = pd.to_numeric(database["day"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["timestamp"]   = pd.to_datetime(database["timestamp"], "coerce", format = "%H:%M:%S").dt.time
                    database                = database.dropna()
                    return database


if __name__ == '__main__':
    pass
