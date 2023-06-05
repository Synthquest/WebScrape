import os
import time
import requests
import pandas as pd
from dotenv import dotenv_values

# Get the absolute path of the .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load API key and search engine ID from .env file
config = dotenv_values(env_path)
API_KEY = config['Google-Search-Key']
SEARCH_ENGINE_ID = config['Google-Search-ID']

# Read the existing descriptions from the CSV file (if it exists)
existing_df = pd.DataFrame()
if os.path.exists('descriptions.csv'):
    existing_df = pd.read_csv('descriptions.csv')

# Create a dictionary to store the existing descriptions by link
existing_descriptions = existing_df.set_index('Link')['Description'].to_dict()

# Read the CSV file into a DataFrame
df = pd.read_csv('descriptions.csv')

# Create empty lists for storing descriptions and links
descriptions = []
links = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    description = row['Description']
    link = row['Link']
    
    # Check if a description already exists in the Descriptions column for the link
    if pd.isna(description) or str(description).strip() == '':
        # Construct the API request URL
        url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={link}'
        
        # Make the API request
        response = requests.get(url)
        data = response.json()
        
        # Check if the API request was successful
        if response.status_code == 200 and 'items' in data:
            try:
                description = data['items'][0]['pagemap']['metatags'][0]['og:description']
            except KeyError:
                description = 'Not found'
        else:
            print(f"Google search failed for link: {link}")
            description = ''
        
        # Add the newly retrieved description to the existing_descriptions dictionary
        existing_descriptions[description] = description
        print(f"Description added for: {link}")
    else:
        existing_descriptions[description] = description
        print(f"Description already Exists for: {link}")
    
    # Append the description and link to the respective lists
    descriptions.append(description)
    links.append(link)
    
    # Add a delay of 5 seconds between each search request
    time.sleep(0)

# Create a new DataFrame with the descriptions and links
result_df = pd.DataFrame({'Description': descriptions, 'Link': links})

# Export the result DataFrame to a CSV file
result_df.to_csv('descriptions.csv', index=False)

print("Descriptions exported successfully!")
