import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

# get env variables
DUNE_API_KEY = os.environ.get('X-Dune-Api-Key')

api_key = DUNE_API_KEY

# Set the csv_file_path to the file 'staking_ratio.csv' in the current working directory
csv_file_path = os.path.join(os.getcwd(), 'CexVentures.csv') 
# csv_file_path = '/path/to/your/file.csv'  # Set the csv_file_path to an explicit file path


url = 'https://api.dune.com/api/v1/table/upload/csv'

with open(csv_file_path, encoding='utf-8') as open_file:
    data = open_file.read()
    
    headers = {'X-Dune-Api-Key': api_key}

    payload = {
        "table_name": "CEX Ventures",
        "description": "CEX ventures + links - maintained: https://github.com/Synthquest/WebScrape",
        "data": str(data)
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print('Response status code:', response.status_code)
    print('Response content:', response.content)
