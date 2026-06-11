import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for item in soup.find_all("div", class_="quote"):
    quote = item.find("span", class_="text").text
    author = item.find("small", class_="author").text

    quotes.append(quote)
    authors.append(author)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv(
    r"D:\HexSoftwares_Python_Programming\HexSoftwarePP_Task-2\Task2_Project1_Web_Scraper\output.csv",
    index=False
)
print("Data scraped successfully!")
print(data.head())