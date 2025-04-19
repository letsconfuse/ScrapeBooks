# Book Scraper Project

This repository contains a Python script that scrapes book data from the website [Books to Scrape](http://books.toscrape.com/). The script uses `requests` and `BeautifulSoup` for web scraping, and saves the extracted data into a CSV file. It also features user input handling, progress display via `tqdm`, and error management.

## Files

- `main.py`: The main Python script that performs the scraping operation.

## Features

- Asks user how many pages they want to scrape (1–1000 range).
- Scrapes each book’s:
  - Title
  - Price
  - Availability
- Combines data from multiple pages.
- Saves output as a timestamped CSV file.
- Shows scraping progress with a progress bar.
- Handles request errors and user interruptions.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed and the following packages:

```bash
pip install requests beautifulsoup4 tqdm
```

### Running the Script

1. Clone the repository:

```bash
git clone https://github.com/letsconfuse/ScrapeBooks.git
cd ScrapeBooks
```

2. Open a terminal and run:

```bash
python main.py
```

3. Enter the number of pages to scrape when prompted.

4. The script will save the results to a timestamped CSV file in the specified folder path within the script (`save_path`).

### Output

CSV file with columns:
- `Title`
- `Price`
- `Availability`

Saved in the format: `books_YYYYMMDD_HHMMSS.csv`

## Use Cases

- Practice for web scraping in Python
- Gathering mock e-commerce data for testing or projects
- Understanding how to structure a simple scraper with user interaction

## License

This project is licensed under the MIT License.

## Author

[letsconfuse](https://github.com/letsconfuse)

Feel free to fork, modify, or extend this project as you see fit!

