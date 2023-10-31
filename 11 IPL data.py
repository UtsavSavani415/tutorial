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

df = pd.DataFrame(columns=titles)

rows = table.find_all("tr")

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row
    # print(row)

print(df)

df.to_csv("IPL_auction.csv")
