import requests
from bs4 import BeautifulSoup
import json

class WebScraper:
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def scrape_table_data(self):
        response = requests.get(self.url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        table = soup.find('table')

        header_cells = table.find('tr').find_all('th')
        headers = [cell.get_text(strip=True) for cell in header_cells]

        table_data = []

        rows = table.find_all('tr')[1:]
        for row in rows:
            cells = row.find_all('td')[:-1]
            row_data = [cell.get_text(strip=True) for cell in cells]
            table_data.append(row_data)

        table_dict_list = []
        for row in table_data:
            table_dict_list.append(dict(zip(headers, row)))

        with open(self.output_file, 'w') as json_file:
            json.dump(table_dict_list, json_file, indent=4)

        print(f"Extracted table data saved to {self.output_file}")
