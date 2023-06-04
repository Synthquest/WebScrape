import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML code from the file with specified encoding
with open('htmlCode_Binance.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div', class_='portfolio_module_portfolio__image__EgbVw')

# Extract the URLs from the anchor tags and store them in a list
urls = [div.find('a')['href'] for div in div_elements]

# Split the URLs into prefix, body, and suffix
split_urls = []

for url in urls:
    url_parts = url.replace("https://", "").replace("www.", "").replace("http://", "").split(".")  # Remove "https://" and "www." and split by "."
    url_parts = [part.rstrip('/') if part.endswith('/') else part for part in url_parts]  # Remove trailing "/" if present
    url_parts = [part for part in url_parts if part not in ("com", "io", "xyz", "cc")]  # Remove unwanted parts
    split_urls.append(url_parts[0]) # Add only the URL body

# Create a DataFrame from the combined URLs with the original URL included
df = pd.DataFrame({'Venture': split_urls, 'Link': urls})

# Add a new column 'Parent' with the value 'Coinbase'
df.insert(0, 'Parent', 'Binance')

# Add a new column 'Parent' with the value 'Coinbase'
df.insert(2, 'Description', '')

# Export the dataframe to a CSV file
df.to_csv('BinanceVentures.csv', index=False)

print("CSV file exported successfully!")
