import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

response1 = requests.get("http://api.football-data.org/v4/competitions/")
response1.status_code
football = response1.json()
football_doc = football['competitions'][:]

competition_list = []
for c_names in football_doc:
    y = c_names['name']
    competition_list.append(y)

df3 = pd.DataFrame(competition_list, columns=['Competition_list'])

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-central-1")

wr.s3.to_parquet(
    df=df3,
    path="s3://apitest-by-ebun/api_tasks/randomuserprofiles",
    boto3_session=session,
    mode='append',
    dataset=True)
