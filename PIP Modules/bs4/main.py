import requests
from bs4 import BeautifulSoup
from functools import lru_cache 
import csv

path = "index.html"
result = []


@lru_cache(maxsize=32)
def pagination(url_path):
    response = requests.get(f"https://books.toscrape.com/{url_path}")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def book_price_availability(url_path):
    global path
    global result
    book_components = pagination(url_path).find_all('article')
    
    for book in book_components:
        line = []
        line.append(book.find('h3').find('a').get('title'))
        line.append(book.find_all('div')[1].find_all('p')[0].text)
        line.append(book.find_all('div')[1].find_all('p')[1].get_text(strip=True))
        result.append(line)
    
    button = pagination(url_path).find(class_='next')

    if button:
        button_href = button.find('a').get('href')
        if button_href[:10] == "catalogue/":
            path = button_href
        else:
            path = f"catalogue/{button_href}"
    else:
        print(f"INFO - There is no next button in this page {url_path}")
        return 0


def saving_results(csv_file, dataset, headers):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        open_csv_file = csv.writer(file)
        open_csv_file.writerow(headers)
        for row in dataset:
            open_csv_file.writerow(row)


def first_lab():
    while True:
        status = book_price_availability(path)
        if status == 0:
            break 
        print(f"INFO - {path} scraped.")
    try: 
        saving_results('result.csv', result, ["Book Name", "Price", "Availability"])
    except Exception as e: 
        print("ERROR - ", e)


def category_book_counter(path):
    target = pagination(path)
    return target.find(class_='form-horizontal').find('strong').get_text(strip=True)


def second_lab():
    target = pagination("index.html")
    book_categories_results = []
    for item in target.find('div', class_='side_categories').find_all('a'):
        category_path = item.get('href')
        result = (item.get_text(strip=True), category_book_counter(category_path), f"https://books.toscrape.com/{category_path}")
        book_categories_results.append(result)
        print("INFO - Category processed:", item.get_text(strip=True))
    saving_results('second_lab_results.csv', book_categories_results, ["Book Type", "Book Count", "Type URL"])


if __name__ == "__main__":
    #first_lab()
    second_lab()
