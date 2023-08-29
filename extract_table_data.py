import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage containing the table
url = 'https://genshin-impact.fandom.com/wiki/Wonders_of_the_World'

# Fetch the HTML content of the webpage
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Locate the table element on the webpage
table = soup.find('table')

# Locate the table headers (th) to use as keys for the JSON
header_cells = table.find('tr').find_all('th')
headers = [cell.get_text(strip=True) for cell in header_cells]

# Initialize a list to store the extracted data
table_data = []

# Locate all rows within the table (excluding header row)
rows = table.find_all('tr')[1:]  # Exclude header row

# Loop through rows and extract cell data (excluding the last cell)
for row in rows:
    cells = row.find_all('td')[:-1]  # Exclude the last cell
    row_data = [cell.get_text(strip=True) for cell in cells]
    table_data.append(row_data)

# Create a list of dictionaries using headers as keys
table_dict_list = []
for row in table_data:
    table_dict_list.append(dict(zip(headers, row)))

# Save the extracted table data to a JSON file
output_file = 'table_data.json'
with open(output_file, 'w') as json_file:
    json.dump(table_dict_list, json_file, indent=4)

print(f"Extracted table data saved to {output_file}")
