import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
Desc = []
Reviews = []

url = "https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = requests.get(url)


soup = BeautifulSoup(r.text, "lxml")


for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    for i in names:
        n = i.text
        Names.append(n)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")

    for i in prices:
        p = i.text
        Prices.append(p)

    decs = box.find_all("ul", class_="_1xgFaf")

    for i in decs:
        d = i.text
        Desc.append(d)

    review = box.find_all("div", class_="_3LWZlK")

    for i in review:
        r = i.text
        Reviews.append(r)

    # print(Names)
    # print(Prices)
    # print(Desc)
    # print(Reviews)

    print(len(Names))
    print(len(Prices))
    print(len(Desc))
    print(len(Reviews))

    # np = soup.find("a", class_ = "_1LKTO3")
    # np = np.get("href")
    # cnp = "https://www.flipkart.com" + np
    # print(cnp)

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")


df = pd.DataFrame({"Name": Names, "Price": Prices,
                  "Description": Desc, "Reviews": Reviews})

print(df)
df.to_csv("mobiles.csv")
