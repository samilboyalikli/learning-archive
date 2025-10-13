import requests
from bs4 import BeautifulSoup
from functools import lru_cache 
import csv


@lru_cache(maxsize=32)
def pagination(path):
    response = requests.get(f"https://books.toscrape.com/{path}")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def book_price_availability(path):
    book_components = pagination(path).find_all('article')
    dataset = []    
    
    for book in book_components:
        line = []
        line.append(book.find('h3').find('a').get('title'))
        line.append(book.find_all('div')[1].find_all('p')[0].text)
        line.append(book.find_all('div')[1].find_all('p')[1].get_text(strip=True))
        dataset.append(line)
    
    return dataset
    
    button = pagination(path).find(class_='next')
    if button:
        return button.find('a').get('href')
    else:
        return 0


def main():
    if book_price_availability("index.html"):
        print(book_price_availability("index.html"))
    else: 
        print("0")
    #button = pagination("index.html").find(class_='next')
    
    #if button:
        #next_page_url = button.find('a').get('href')
        #book_price_availability(next_page_url)
        


if __name__ == "__main__":
    main()

