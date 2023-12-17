#%%
import  pandas              as pd
import  numpy               as np
from    dateutil.parser     import parse



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
            #ADDITIONAL SUPPORT METHODS > NOTE: TYPE self. BEFORE USING
            def list_join(self, l):
                        try:
                            return ','.join(map(str, l))
                        except TypeError:
                            return np.nan



            #T3
            #CLEAN USER
            def clean_user_data(self,database):
                    #REMOVED INVALID user_uuid > Assuming we cannot track invalid user_uuid across the schema database.
                    database["uuid_length"]         = database["user_uuid"].str.len()
                    database                        = database.drop(database[database["uuid_length"] < 30].index)

                    #CONVERT ALL DATES INTO A STANDARDISED FORMAT
                    database["dob"]                 = database["date_of_birth"].apply(parse)
                    database["joind"]               = database["join_date"].apply(parse)
                    database["date_of_birth"]       = database["dob"]
                    database["join_date"]           = database["joind"]

                    #CORRECT TYPO IN COUNTRY CODE
                    database["country_code"]        = database["country_code"].replace("GGB","GB")

                    #DROP COLUMNS
                    database                        = database.reset_index()
                    database                        = database.drop(columns=["index","level_0","uuid_length","dob","joind"])

                    #FIXING THE PHONE NUMBERS (TAKEN FROM AI_CORE NOTES)
                    regex_expression = '^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$' #Our regular expression to match
                    database.loc[~database["phone_number"].str.match(regex_expression), "phone_number"] = np.nan # For every row  where the Phone column does not match our regular expression, replace the value with NaN

                    database["phone_number"]        = database["phone_number"].str.replace('+44(0)', '0', regex=False)
                    database["phone_number"]        = database["phone_number"].str.replace('+44', '0', regex=False)
                    database["phone_number"]        = database["phone_number"].str.replace('(', '', regex=False)
                    database["phone_number"]        = database["phone_number"].str.replace(')', '', regex=False)
                    database["phone_number"]        = database["phone_number"].str.replace(' ', '', regex=False)

                    #FIXING ADDRESS
                    database["address"]             = database["address"].str.replace('\n', ', ', regex=False)
                    database["address"]             = database["address"].str.replace('/', '', regex=False)

                    return database

            #T4
            #CLEAN CARD DETAILS
            def clean_card_details(self, database):
                    #CARD PROVIDER LIST
                    card_provider_list                          = [ "VISA 16 digit" , "JCB 16 digit" , "VISA 13 digit" , "JCB 15 digit" , "VISA 19 digit" , "Diners Club / Carte Blanche" , "American Express" , "Maestro" , "Discover" , "Mastercard" ]
                    database["listed"]                          = database["card_provider"].isin(card_provider_list)

                    #REMOVING False LISTINGS, INDEX RESET & DROPPING COLUMNS
                    database                                    = database.drop(database[database["listed"] == False].index)
                    database                                    = database.reset_index()
                    database                                    = database.drop(columns=["index","listed"])

                    #CONVERT ALL DATES INTO A STANDARDISED FORMAT
                    database["date_payment_confirmed"]          = database["date_payment_confirmed"].apply(parse)
                    database["date_payment_confirmed"]          = database["date_payment_confirmed"]
                    
                    return database
            
            #T5
            #CLEAN STORE DETAILS
            def clean_store_data (self, database):
                    #REMOVED INVALID country_code > This will in turn target our void data.
                    database                        = database.reset_index()
                    database                        = database.drop(columns= ["level_0" , "index"])
                    database["cc_length"]           = database["country_code"].str.len()
                    database                        = database.drop(database[database["cc_length"] > 2].index)

                    #database["strings_1"]           = database["staff_numbers"].str.isnumeric()

                    #CONVERT ALL DATES INTO A STANDARDISED FORMAT
                    database["open_date"]           = database["opening_date"].apply(parse)
                    database["opening_date"]        = database["open_date"]

                    #TRANSPOSE latitude data into lat and rename lat into latitude whilst dropping original latitude
                    database["lat"]                 = database["latitude"]
                    database                        = database.drop(columns=["latitude" , "cc_length" , "open_date"])
                    database                        = database.rename({"lat" : "latitude"}, axis=1)

                    #REMOVE LETTERS FROM COLUMN (STAFF_NUMBER)
                    #import numpy as np

                    database["staff_numbers"] = database["staff_numbers"].str.split("\D")

                        #use list join
                    database["staff_numbers"] = [self.list_join(l) for l in database["staff_numbers"]]
                    database["staff_numbers"] = database["staff_numbers"].replace(',','', regex=True)

                    #ADJUST DATA TYPES
                    database["staff_numbers"]       = pd.to_numeric(database["staff_numbers"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["longitude"]           = pd.to_numeric(database["longitude"], "coerce", "float", dtype_backend="numpy_nullable")
                    database["latitude"]            = pd.to_numeric(database["latitude"], "coerce", "float", dtype_backend="numpy_nullable")


                    #CORRECT CONTINENTS EUROPE AND AMERICA
                    database["continent"] = database["continent"].replace("eeEurope","Europe")
                    database["continent"] = database["continent"].replace("eeAmerica","America")

                    #FIX INDEX
                    database                        = database.reset_index()
                    database                        = database.drop(columns= "index")

                    return database

            #T6
            #CLEAN PRODUCTS DATA
            def clean_products_data (self, database):
                    database                        = database.rename(columns={"uuid":"product-uuid"})
                    database                        = database.rename(columns={"removed":"still_available"})
                    category_list                   = ["homeware", "toys-and-games", "food-and-drink", "pets", "sports-and-leisure", "health-and-beauty", "diy"]
                    database["category_in_list"]    = database["category"].isin(category_list)
                    database                        = database.drop(database[database["category_in_list"] == False].index)
                    database                        = database.drop(columns=["category_in_list"])

                    #CONVERT ALL DATES INTO A STANDARDISED FORMAT
                    database["date_added"]          = database["date_added"].apply(parse)
                    database["date_added"]          = database["date_added"]

                    #STRIP OUT ALL THE WEIGHT AND PUT IT ALL BACK TOGETHER AGAIN IN KILOGRAM
                    #Seperate the weight classes
                    database[["kilo-weight", "unit"]]               = (database["weight"].str.split("kg", n=1, expand=True))
                    database[["gram-weight", "unit"]]               = (database["weight"].str.split("g", n=1, expand=True))
                    database[["ml-weight", "unit"]]                 = (database["weight"].str.split("ml", n=1, expand=True))
                    database[["oz-weight", "unit"]]                 = (database["weight"].str.split("oz", n=1, expand=True))

                    database[["Multiplier", "unit-weight"]]         = (database["weight"].str.split(" x ", n=1, expand=True))
                    database[["unit-weight", "unit"]]               = (database["unit-weight"].str.split("g", n=1, expand=True))

                    #Change types to INTEGERS for MATHS operations
                    database["kilo-weight"]             = pd.to_numeric(database["kilo-weight"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["gram-weight"]             = pd.to_numeric(database["gram-weight"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["ml-weight"]               = pd.to_numeric(database["ml-weight"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["oz-weight"]               = pd.to_numeric(database["oz-weight"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["Multiplier"]              = pd.to_numeric(database["Multiplier"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["unit-weight"]             = pd.to_numeric(database["unit-weight"], "coerce", "integer", dtype_backend="numpy_nullable")

                    #CONVERSION Calculations
                    database["gram_calc"]               = database["Multiplier"].values * database["unit-weight"].values

                    database["gram-weight"]             = database["gram-weight"] / 1000        #converted into kg
                    database["ml-weight"]               = database["ml-weight"] / 1000          #converted into kg (using a 1:1 ratio with grams)
                    database["oz-weight"]               = database["oz-weight"] * 0.028349523   #converted into kg

                    #DROP COLUMNS & CREATE COMBINED
                    database                            = database.drop(columns=["unit", "Multiplier" , "unit-weight"])
                    database["combined"]                = database[database.columns[9:]].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1 )
                    database                            = database.drop(columns=["kilo-weight","gram-weight", "ml-weight", "oz-weight", "gram_calc"])

                    #CONVERSION DONE - RE-ESTABLISH BASE COLUMN
                    database["weight"]                  = database["combined"]
                    database                            = database.drop(columns=["combined"])
                    database["weight"]                  = pd.to_numeric(database["weight"], "coerce", "float", dtype_backend="numpy_nullable")
                    database                            = database.rename(columns={"weight":"weight_(kg)"})

                    #REMOVE CURRENCY £ FROM Product_price
                    database["product_price"]           = database["product_price"].str.replace("£","")
                    database                            = database.rename(columns={"product_price":"product_price_(£)"})


                    #WEIGHT CLASS
                    #Defining class conditions as columns > Results in boolean
                    database["light"]                   = database["weight_(kg)"] < 2
                    database["mid-sized"]               = (database["weight_(kg)"] >= 2) & (database["weight_(kg)"] < 40)
                    database["heavy"]                   = (database["weight_(kg)"] >= 40) & (database["weight_(kg)"] < 140)
                    database["truck"]                   = database["weight_(kg)"] >= 40

                    #Creating Weight Class and inputting human-readable values
                    database.loc[database["light"],     "weight_class"] = "Light"
                    database.loc[database["mid-sized"], "weight_class"] = "Mid_Sized"
                    database.loc[database["heavy"],     "weight_class"] = "Heavy"
                    database.loc[database["truck"],     "weight_class"] = "Truck_Required"

                    #FIXING INCORRECT EAN CODES  -->> This is a bold attempt at guessing what the code should of been as there appears to be a pattern in the alteration by using repeated 1,2,3 & 4 characters together.
                    database["EAN"] = database["EAN"].str.replace("22225010240729109","5010240729109")
                    database["EAN"] = database["EAN"].str.replace("335080471900288","5080471900288")
                    database["EAN"] = database["EAN"].str.replace("44440472306810827","0472306810827")
                    database["EAN"] = database["EAN"].str.replace("113231613960017","3231613960017")
                    database["EAN"] = database["EAN"].str.replace("17132118932225","7132118932225")

                    #DROP COLUMNS
                    database                            = database.drop(columns=["light", "mid-sized", "heavy", "truck"])
                    database                            = database.reset_index()
                    database                            = database.drop(columns=["index"])  
                    
                    return database

            #T7
            #CLEAN ORDERS DATA
            def clean_orders_data (self, database):
                    database        = database.drop(columns= ["level_0", "index", "1", "first_name", "last_name"] )
                    database        = database.reset_index()
                    database        = database.drop(columns= "index" ) 

                    return database

            #T8
            #CLEAN DATE TIMES
            def clean_date_times (self, database):
                    database["month"]       = pd.to_numeric(database["month"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["year"]        = pd.to_numeric(database["year"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["day"]         = pd.to_numeric(database["day"], "coerce", "integer", dtype_backend="numpy_nullable")
                    database["timestamp"]   = pd.to_datetime(database["timestamp"], "coerce", format = "%H:%M:%S").dt.time
                    database                = database.dropna()
                    database                = database.reset_index()
                    database                = database.drop(columns= "index" )
                    return database


if __name__ == '__main__':
    pass
