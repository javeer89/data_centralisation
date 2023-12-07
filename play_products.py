#%%
import boto3
import pandas as pd


def extract_from_s3():
        s3 = boto3.client("s3")
        s3.download_file("data-handling-public", "products.csv","jav-products.csv" )  
        df = pd.read_csv('jav-products.csv')

        return df

extract_from_s3()



        