import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


response2 = requests.get("https://randomuser.me/api/?results=500")
response2.status_code
my_doc = response2.json()
my_new_doc = my_doc['results'][:]

# subtask1: Extracting all male and female profiles into a different list
male_profile = []
female_profile = []
gender = []
for item in my_new_doc:
    gender.append(item['gender'])
    if item['gender'] == 'male':
        male_profile.append(item)
    elif item['gender'] == 'female':
        female_profile.append(item)

# subtask2: Extract all dob date into a list(date_list).
date_list = []
for item in my_new_doc:
    date_list.append(item['dob']['date'])

full_name = []
for names in my_new_doc:
    first_name = names['name']['first']
    last_name = names['name']['last']
    concat_name = first_name + ' ' + last_name
    full_name.append(concat_name)

randomuserprofile = {
    'full_name': full_name,
    'gender': gender,
    'dob': date_list
}

