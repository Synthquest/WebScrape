from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML code from the file with specified encoding
with open('htmlCode_DCG.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all instances of divs with the updated class attribute value
interactable_divs = soup.find_all(class_="folio__item")

# Extract the data and store them in a list
data = []
for div in interactable_divs:
    venture = div.get("data-order")
    description_element = div.find(class_="portfolio__item-desc text-body-small is--t-gray11 margin-bottom-24")
    link_element = div.find(class_="item__sitelink text-body-small is--t-black margin-bottom-12 w-inline-block")
    if venture and description_element and link_element:
        description = description_element.get_text(strip=True)
        link = link_element['href']
        data.append([venture, description, link])

# Create a dataframe from the data list
df = pd.DataFrame(data, columns=['Venture', 'Description', 'Link'])

# Update the 'Parent' column to 'DCG'
df.insert(0, 'Parent', 'DCG')

# Export the dataframe to a CSV file
df.to_csv('DCGVentures.csv', index=False)

print("CSV file exported successfully!")
