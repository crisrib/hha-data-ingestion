## import packages
import pandas as pd 
import json 
import bs4 
import requests 
import sqlalchemy 
from PIL import Image  
import pydub 
from pydub.playback import play
import playsound 
import geopandas as gpd 
from google.cloud import bigquery 
import matplotlib
import xlrd 
import PyPDF2

## Section 1: Find or create 1 excel (.xls) file that contains at least two tabs. Bring in the first tab as a data frame; label that dataset as ‘tab1’, and a second data frame that represents the 2nd tab of the excel file, name this 'tab2'
df = pd.read_excel('Data/dataset-for-hw1.xlsx')
tab_1 = pd.read_excel('Data/dataset-for-hw1.xlsx', sheet_name='Perpetrators_by_Relationship_to')
tab_1
tab_2 = pd.read_excel('Data/dataset-for-hw1.xlsx', sheet_name='Maltreatment_Types_of_Victims')
tab_2

## Section 2: Find 1 open source json API via CMS, and bring it in using the 'requests' package ; call the dataset ‘apiDataset’ 
## Get data request from https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data
r_data = requests.get('https://data.cms.gov/data-api/v1/dataset/7171ef6c-a2cf-43d4-b8ab-774b0de9b90a/data')
## Load as JSON
dataset = r_data.json()
## Load into dataframe
df = pd.DataFrame.from_records(dataset)
df

## Section 3: Bring in 2 open source bigquery datasets; limit your query to get the first 100 rows from each, as either a dataframe or dictionary; please call the first dataset ‘bigquery1’ and the second dataset ‘bigquery2’
client = bigquery.Client.from_service_account_json('ingestion/example_files/bigquery/hants-507-0569c50b5a7c.json')
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results = query_job.result()
query_job_2 = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100")
results_2 = query_job_2.result()
bigquery2 = pd.DataFrame(results_2.to_dataframe())
