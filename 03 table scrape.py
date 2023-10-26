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

ds = pd.DataFrame(columns=titles)

print(ds)