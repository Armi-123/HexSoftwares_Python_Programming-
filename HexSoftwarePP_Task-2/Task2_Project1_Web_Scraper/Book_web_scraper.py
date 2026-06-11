import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = []
prices = []
ratings = []

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

data = pd.DataFrame({
    "Book Title": titles,
    "Price": prices,
    "Rating": ratings
})

data.to_csv(
    "HexSoftwarePP_Task-2/Task2_Project1_Web_Scraper/books_data.csv",
    index=False
)
# Task2_Project1_Web_Scraper
print("\nData Scraped Successfully!")
print(data.head())