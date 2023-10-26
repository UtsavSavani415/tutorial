import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r= requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_ ="title")

# print(names)

product_name = []

for i in names:
    name = i.text
    product_name.append(name)

# print(product_name)



    # price
prices = soup.find_all("h4", class_ = "price")

product_price = []

for i in prices:
    price = i.text
    product_price.append(price)

# print(product_price)

# desc
descriptions = soup.find_all("p", class_ = "description")

product_description = []

for i in descriptions:
    description = i.text
    product_description.append(description)

# print(product_description)


# pandas data

df = pd.DataFrame({"Product Name":product_name, "Product Price": product_price, "Product Description": product_description})

print(df)

# df.to_csv("product_details.csv")