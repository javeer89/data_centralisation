#%%
import  pandas          as pd
import  numpy           as np
import  phonenumbers


class DataCleaning:
    '''clean data from each of the data sources'''

    def __init__(self) -> None:
        pass
    
    #data cleaning tools

    #adjust dates to format into correct form
    def clean_date(self, database, column_name):
        database[column_name] = pd.to_datetime(database[column_name], errors='ignore', format= '%Y %b %d')

    #clean phone numbers and make them into a standardised format    
    def clean_phone_numbers(self, database, column_name):
        database[column_name]

    def clean_country_code(self, database, column_name):
        database[column_name]


    def clean_na_null(self, database, column_name):
        database[column_name] = database.replace(np.nan, None)
        database[column_name]


    #data clean method
    def clean_user_data(self,database):
        #remove first column
        database.drop(columns='1',inplace=True)

        #check dates in date_of_birth and join_date
        database = self.clean_date(database,'date_of_birth')
        database = self.clean_date(database,'join_date')

        #
        
        #check phone numbers and check country code
        database = self.clean_phone_numbers(database, 'phone_number')
        database = self.clean_country_code(database, 'country_code')


        #


        #removes Na and Null values
        database = self.clean_na_null(database)

        return database




