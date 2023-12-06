#%%
import  pandas          as pd
import  numpy           as np
import  phonenumbers

#data cleaning tools
class DataCleaning:
    '''clean data from each of the data sources'''
    ''' from data_analysis.py it has been determined that there are: 
            - no na values
            - no null values.
            - no duplicates

        actions to be undertaken, are as follows:
            - remove index column as there are mistakes in it. use native index.   
    '''
    
    def __init__(self) -> None:
        pass
  
    def drop_index(self, database, column_name):
        database.drop(column = [column_name])

    #adjust dates to format into correct form
    def clean_date(self, database, column_name):
        database[column_name] = pd.to_datetime(database[column_name], errors='ignore', format= '%Y %b %d')

    #clean phone numbers and make them into a standardised format    
    def clean_phone_numbers(self, database, column_name):
        database[column_name]

    def clean_country_code(self, database, column_name):
        database[column_name]


    

    #CLEAN USER
    def clean_user_data(self,database):
        #1  - drop index
        database = self.drop_index(database,"index")

        #2  - removes Na and Null values
        #database = self.clean_na_null(database, 'date_of_birth')
        #database = self.clean_na_null(database, 'join_date')

        #3  - check dates in date_of_birth and join_date
        #self.database = self.clean_date(database,'date_of_birth')
        #database = self.clean_date(database,'join_date')


        #check phone numbers and check country code
        #database = self.clean_phone_numbers(database, 'phone_number')
        #database = self.clean_country_code(database, 'country_code')


        return database




