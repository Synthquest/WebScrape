import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML code from the file with specified encoding
with open('htmlCode_a16z.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div', class_='company')

# Extract the venture name and link from each div element
ventures = []
descriptions = []
links = []
for div in div_elements:
    # Check if an anchor tag exists within the div
    anchor = div.find('a')
    if anchor:
        # Extract the venture name from the href attribute of the anchor tag
        venture = anchor.get('href')
        venture = venture.replace("https://", "").replace("www.", "").replace("http://", "").replace("app.", "").split(".")[0]
        ventures.append(venture)

        # Extract the link from the href attribute of the anchor tag
        link = anchor.get('href')
        links.append(link)

        # Set an empty description for each div element
        descriptions.append('')
    else:
        # If anchor tag is not found, skip this div
        continue

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Venture': ventures, 'Description': descriptions, 'Link': links})

# Add a new column 'Parent' with the value 'a16z'
df['Parent'] = 'a16z'

# Reorder the columns
df = df[['Parent', 'Venture', 'Description', 'Link']]

# Export the dataframe to a CSV file
df.to_csv('a16zVentures.csv', index=False)

print("CSV file exported successfully!")
