import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
from tqdm import tqdm  # Progress bar library

def get_valid_page_count(max_pages=1000):
    while True:
        try:
            num_pages = int(input(f"How many pages do you want to scrape? (1-{max_pages}): "))
            if 1 <= num_pages <= max_pages:
                return num_pages
            else:
                print(f"❌ Please enter a number between 1 and {max_pages}.")
        except ValueError:
            print("❌ Invalid input. Enter a valid number.")

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return None

def scrape_books_from_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    book_data = []

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        availability = book.find('p', class_='instock availability').text.strip()
        book_url = base_url + book.h3.a['href']  # Get the book's detail page URL

        book_data.append([title, price, availability])

    return book_data

def save_to_csv(data, save_path, timestamp=None):
    if not data:
        print("⚠️ No data to save.")
        return

    if not timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(save_path, f'books_{timestamp}.csv')

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])
        writer.writerows(data)

    print(f"\n✅ Data saved to: {file_path}")

def main():
    global base_url
    base_url = "http://books.toscrape.com/"
    catalogue_url = "http://books.toscrape.com/catalogue/page-{}.html"

    save_path = r"E:\00_E\Code_Programs\VS_Code\Python\ScrapeBooks"
    os.makedirs(save_path, exist_ok=True)

    # User Input for pages
    num_pages = get_valid_page_count()

    all_books = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        for page in tqdm(range(1, num_pages + 1), desc="Scraping Progress", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} pages scraped"):
            url = base_url if page == 1 else catalogue_url.format(page)
            print(f"\rScraping page {page}/{num_pages}...", end="")
            html_content = fetch_page_content(url)

            if html_content:
                books = scrape_books_from_page(html_content)
                all_books.extend(books)
            else:
                print(f"\rSkipping page {page} due to fetch error.", end="")

    except KeyboardInterrupt:
        print("\n⛔ Scraping interrupted by user.")
        save_to_csv(all_books, save_path, timestamp)
        return

    except Exception as e:
        print(f"\n⚠️ An unexpected error occurred: {e}")
        save_to_csv(all_books, save_path, timestamp)
        return

    if all_books:
        save_to_csv(all_books, save_path, timestamp)
    else:
        print("❌ No data scraped.")

if __name__ == "__main__":
    main()
