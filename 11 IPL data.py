import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="ih-td-tab auction-tbl")

header = table.find_all("th")

titles = []

teams = []

fund_remains = []


for i in header:
    title = i.text
    titles.append(title)


rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    print(row)

df = pd.DataFrame(columns=titles)
# print(df)
