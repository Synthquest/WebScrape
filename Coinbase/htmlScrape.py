from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML code from the file with specified encoding
with open('htmlCode_Coinbase.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all instances of divs with the updated class attribute value
interactable_divs = soup.find_all(class_="cds-interactable-i9xooc6 cds-transparentChildren-tnzgr0o cds-focusRing-fd371rq cds-transparent-tlx9nbb cds-pressableResetStyles-p1yut83c")

# Extract the pairs and store them in a list
pairs = []
for div in interactable_divs:
    title_element = div.find(class_="Text-sc-1ytabpv-0 ktFOpz")
    description_element = div.find(class_="Text-sc-1ytabpv-0 ktYgkv")

    if title_element and description_element:
        title = title_element.get_text(strip=True)
        description = description_element.get_text(strip=True)
        pairs.append([title, description])

# Create a dataframe from the pairs list
df = pd.DataFrame(pairs, columns=['Venture', 'Description'])

# Add a new column 'Parent' with the value 'Coinbase'
df.insert(0, 'Parent', 'Coinbase')

# Add a new column 'Parent' with the value 'Coinbase'
df.insert(3, 'Link', '')

# Export the dataframe to a CSV file
df.to_csv('CoinbaseVentures.csv', index=False)

print("CSV file exported successfully!")
