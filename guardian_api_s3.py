import os

import awswrangler as wr
import boto3
from dotenv import load_dotenv

from guardian_api_extract import extract

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
API_KEY = os.getenv('API_KEY')
url ='https://content.guardianapis.com/search?page=1&q="nigeria"&from-date=2025-01-01&api-key={API_KEY}'
df = extract(url)


session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-central-1")

wr.s3.to_parquet(
    df=df,
    path="s3://apitest-by-ebun/api_tasks/guardian_file/",
    boto3_session=session,
    mode='append',
    dataset=True
)
