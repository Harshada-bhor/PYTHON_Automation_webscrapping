#Links Extractor using Web Scrapping

import bs4
from sys import *
import os
import requests
from urllib.parse import urlparse


def MarvellousLinksDisplay(url):
    res = requests.get(url)
    print(type(res))

    soup = bs4.BeautifulSoup(res.text)
    print(type(soup))

    links = soup.find_all("a",href = True)

    return links


def main():
    print("___________Python Automation & Machine learning __________")
    
    url='https://en.wikipedia.org/wiki/python_(programming_language)'

    arr = MarvellousLinksDisplay(url)

    print("Links are ")

    for element in arr:
       if "#" not in element["href"]:
           print(element["href"])

if (__name__ == "__main__"):
    main()
