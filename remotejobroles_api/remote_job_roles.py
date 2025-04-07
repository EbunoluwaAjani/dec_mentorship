import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Task1: Extract all senior roles and manager roles into a different list.
url = (
    "https://jobicy.com/api/v2/remote-jobs"
    "?count=20&geo=usa&industry=marketing&tag=seo"
)
response = requests.get(url)
print(f"Status Code: {response.status_code}")
remotejobs = response.json()
Senior_Role = []
Manager_Role = []
for details in remotejobs['jobs']:
    if 'Senior' in details['jobTitle'] or details['jobLevel'] == 'Senior':
        Senior_Role.append(details['jobTitle'])
    elif 'Manager' in details['jobTitle']:
        Manager_Role.append(details['jobTitle'])

remoteroles = {
    'Senior_Role': Senior_Role,
    'Manager_Role': Manager_Role
}
df = pd.json_normalize(remoteroles)
print(df)


session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-central-1")

wr.s3.to_parquet(
    df=df,
    path="s3://apitest-by-ebun/api_tasks/remotejobroles/",
    boto3_session=session,
    mode='append',
    dataset=True)

