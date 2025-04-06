import os
import requests
import time
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def request(data):

    '''
    Sends a request to an API using the requests module.
    Args:
        string: base url.
    Returns:
        dict: A paginated response in JSON format.
    '''
    for i in range(10):
        response = requests.get(data)
        res = response.status_code
        if res == 200:
            file = response.json()
            print(f'Requesting page {i+1} from the base URL')
        else:
            print(f'The status code is {res}')
        time.sleep(2)
        yield file


def extract(base_url):
    '''
    Extracts from an API request function, converts to df and exports to a CSV.

    Args:
        yield value from the inner request function

    Returns:
        CSV-formatted file
    '''
    extracted_file = []
    raw_data = []
    for i in request(base_url):
        row = {}
        row['new1'] = i
        raw_data.append(row)
    print(f'Extracting a total of {len(raw_data)} pages from the base URL')
    for new in raw_data:
        article = new['new1']['response']['results']
        for details in article:
            extracted_file.append(details)
    df = pd.DataFrame(extracted_file)
    print('Data completely processed')
    return df
