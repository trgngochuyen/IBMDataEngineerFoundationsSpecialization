from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
response = requests.get(url) 
html_data = response.text.encode('cp1252', errors='ignore')

soup = BeautifulSoup(html_data, 'html.parser')

table = soup.find("table", "wikitable sortable mw-collapsible")

rows = []

for tablerows in table.find_all("tr"):
    row = []
    for td in tablerows:
        try:
            row.append(td.text.replace('\n', ''))
        except:
            continue
    if len(row) > 0:
        rows.append(row)
        
df = pd.DataFrame(rows[1:], columns=rows[0])
print(df)