#%%
import pandas as pd
from main import database

database

#%%
#returns boolean of database for nulls
print('database.isnull()')
database.isnull()

#%%
#returns boolean of database for null as a column info
print('database.isnull().any()')
database.isnull().any()

#%%
#returns sum of null values
print('database.isnull().sum()')
database.isnull().sum()

#%%
#returns count if there even is a null value
print('database.isnull().any().sum()')
database.isnull().any().sum()

#%%
#returns boolean of database for na
print('database.isna()')
database.isna()

#%%
#returns boolean of database for na as a column info
print('database.isna().any()')
database.isna().any()

#%%
#returns sum of na values
print('database.isna().sum()')
database.isna().sum()

#%%
#returns count if there even is a na value
print('database.isna().any().sum()')
database.isna().any().sum()

#%%
#check for duplicates
print('database.duplicated()')
database.duplicated()#.sum()

#%%
#remove index column

database.drop(columns = "index")
#we want to keep this one.