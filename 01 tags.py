import requests
from bs4 import BeautifulSoup

# with open("sample.html", "r") as f:
#     html_doc = f.read()

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")

soup = BeautifulSoup(r.text, 'lxml')

print("##########################################################")

tag  = soup.find('p',{"class":"description"})

atb = tag.attrs
# print(atb["class"])
print(tag.string)
# print(soup.title.string, type(soup.title.string))

# print(soup.find_all("div")[1])
