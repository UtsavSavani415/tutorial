import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r  = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

# boxes = soup.find_all("div",class_ = "col-md-4 col-xl-4 col-lg-4")

# print(boxes)

# box = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")[2]

# print(box)

# name = box.find("a").text

# print(name)

# desc = box.find("p", class_ = "description").text

# print(desc)



navbar = soup.find_all("ul", class_ = "nav flex-column", id = "side-menu")[0].text

name = soup.find_all("li", class_ = "active")[0].text

print(name)