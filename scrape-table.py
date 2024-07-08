import requests
from bs4 import BeautifulSoup

url = 'http://example.com/table-page'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    data = [cell.get_text() for cell in cells]
    print(data)
