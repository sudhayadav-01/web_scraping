"""
Task 1: Web Scraping
Scrapes book data (title, price, rating, availability) from
http://books.toscrape.com - a public site made for scraping practice.
Handles HTML parsing + pagination, and saves a custom dataset to CSV.

Install:  pip install requests beautifulsoup4 pandas
Run:      python web_scraper.py
"""

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "http://books.toscrape.com/catalogue/page-1.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (student scraping project)"}
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_soup(url):
    """Download a page and return a BeautifulSoup object."""
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "html.parser")


def parse_books(soup, page_url):
    """Extract book details from one listing page."""
    books = []
    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = float(item.select_one("p.price_color").text.replace("£", "").strip())
        rating_word = item.select_one("p.star-rating")["class"][1]
        availability = item.select_one("p.availability").text.strip()
        link = urljoin(page_url, item.h3.a["href"])

        books.append({
            "title": title,
            "price_gbp": price,
            "rating": RATING_MAP.get(rating_word, 0),
            "availability": availability,
            "url": link,
        })
    return books


def scrape_all(start_url, max_pages=5):
    """Follow the 'next' button to scrape multiple pages (web navigation)."""
    all_books = []
    url = start_url
    page = 1

    while url and page <= max_pages:
        print(f"Scraping page {page}: {url}")
        soup = get_soup(url)
        all_books.extend(parse_books(soup, url))

        next_btn = soup.select_one("li.next a")
        url = urljoin(url, next_btn["href"]) if next_btn else None
        page += 1
        time.sleep(1)  # be polite to the server

    return all_books


def main():
    data = scrape_all(BASE_URL, max_pages=5)

    df = pd.DataFrame(data)
    df.drop_duplicates(subset="title", inplace=True)

    # Custom dataset: only books rated 4+ and under £30
    custom = df[(df["rating"] >= 4) & (df["price_gbp"] < 30)]

    df.to_csv("books_all.csv", index=False)
    custom.to_csv("books_custom.csv", index=False)

    print(f"\nTotal books scraped : {len(df)}")
    print(f"Custom dataset size : {len(custom)}")
    print(f"Average price       : £{df['price_gbp'].mean():.2f}")
    print("\nSample:")
    print(custom.head())


if __name__ == "__main__":
    main()