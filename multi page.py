import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(2,11):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    np = soup.find("a", class_ = "_1LKTO3")
    np = np.get("href")
    cnp = "https://www.flipkart.com" + np
    print(cnp)  

    # url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, "lxml")

