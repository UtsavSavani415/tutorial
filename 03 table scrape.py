import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"

r= requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "table table-sm table-hover screenertable")


headers = table.find_all("th")

titles = []

for i in headers:
    title = i.text
    titles.append(title)

print(titles)

df = pd.DataFrame(columns=titles)



rows = soup.find_all("tr", class_ = "")

for i in rows[1:]:
    data = i.find_all("td")

    # print(data)
    row = [tr.text for tr in data]
    # print(row)
    l = len(df)
    if(len(row)>0):
        df.loc[l] = row
    # print(l)

# print(rows)

print(df)