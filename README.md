# 📚 Web Scraping Project (Python + BeautifulSoup)

A beginner-friendly web scraping project that extracts book data from [Books to Scrape](http://books.toscrape.com), a public website built for scraping practice. The script handles HTML parsing, page navigation (pagination) and saves custom datasets in CSV format.

## ✨ Features

- Extracts **title, price, rating, availability and URL** of each book
- Navigates through multiple pages using the "Next" button
- Cleans data (price conversion, star rating to number, duplicate removal)
- Creates a **custom dataset** (books rated 4+ and priced under £30)
- Saves output as CSV files, ready for analysis in Excel or Pandas

## 🛠️ Tech Stack

- Python 3
- Requests: to download web pages
- BeautifulSoup4: to parse HTML
- Pandas: to clean and save data

## 📁 Project Structure

```
web-scraping/
│── web_scraper.py     # main script
│── books_all.csv      # output: all scraped books
│── books_custom.csv   # output: filtered dataset
│── README.md
```

## ⚙️ Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/web-scraping.git
   cd web-scraping
   ```

2. (Optional) Create a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## ▶️ Usage

```bash
python web_scraper.py
```

No input is required. The script scrapes 5 pages (100 books) by default.

### Customize

| What to change | Where |
|---|---|
| Website URL | `BASE_URL` at the top of `web_scraper.py` |
| Number of pages | `max_pages=5` inside `main()` |
| Filter for custom dataset | `custom = df[(df["rating"] >= 4) & (df["price_gbp"] < 30)]` |

## 🧠 How It Works

1. Sends an HTTP request to the page using `requests`
2. Parses the HTML with `BeautifulSoup` using CSS selectors
3. Finds the "Next" button link and moves to the next page
4. Stores everything in a Pandas DataFrame
5. Cleans the data, applies filters and exports to CSV

## ⚠️ Disclaimer

This project is for **educational purposes only**. Always check a website's `robots.txt` and terms of service before scraping.

## 👩‍💻 Author

**Sudha Yadav**
BCA Student
[LinkedIn](https://linkedin.com/in/sudha-yadav-0b5639374)
