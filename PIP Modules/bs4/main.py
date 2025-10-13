import requests
from bs4 import BeautifulSoup
from functools import lru_cache 
import csv


@lru_cache(maxsize=32)
def fetch_page(url):
    response = requests.get(url)
    return response


soup = BeautifulSoup(fetch_page("https://books.toscrape.com/catalogue/category/books_1/index.html").content, 'html.parser')
soup.find_all('a', limit=5)


def book_and_price():
    book_components = soup.find_all('article')
    dataset = []    
    
    for book in book_components:
        line = []
        line.append(book.find('h3').find('a').get('title'))
        line.append(book.find_all('div')[1].find_all('p')[0].text)
        dataset.append(line)
    
    return dataset


def main():
    print(book_and_price())


if __name__ == "__main__":
    main()

