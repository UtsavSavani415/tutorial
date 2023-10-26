import requests
from bs4 import BeautifulSoup
import re

# with open("sample.html", "r") as f:
#     html_doc = f.read()

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")

soup = BeautifulSoup(r.text, 'lxml')

print("##########################################################")

# tag  = soup.find_all('h4', class_ ="pull-right")

# atb = tag.attrs
# print(atb["class"])
# print(tag)

# for i in tag:
#     print(i.text)
# print(soup.title.string, type(soup.title.string))

# print(soup.find_all("div")[1])

# data = soup.find_all(string="Galaxy Tab")

data = soup.find_all(string=re.compile("Galaxy"))

print(data)


