from bs4 import BeautifulSoup
import requests
import os
import csv
from scraping import scraping_one_product


url = 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'


#Fonction recréant l'url de chaque produit de la page à partir d'un url relatif
def book_url(relative_link):
    base_url = 'http://books.toscrape.com/catalogue/'
    return base_url + relative_link.replace('../', '')


#Fonction intégrant dans un fichier csv les données recueillies
def create_csv(category, list_product_page):
    os.chdir('C:/Users/julie/PycharmProjects/pythonProject/Fichier_CSV')
    with open(category + '.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=['product_page_url', 'universal_product_code',
                                               'title', 'prices_including_taxes',
                                               'prices_excluding_taxes', 'number_available',
                                               'product_description', 'category',
                                               'review_rating', 'image_url'])
        writer.writeheader()
        for element in list_product_page:
            writer.writerow(element)


#Fonction étendant le scraping des informations d'un produit à tous les produits de la page
def scraping_page_category(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all("h3")
        list_product_page = []

        for product in products:
            relative_link = product.find("a").get("href")
            products_informations = scraping_one_product(book_url(relative_link))
            list_product_page.append(products_informations)
        print(list_product_page, 'dtu')
        category_name = soup.find("h1").text
        create_csv(category_name, list_product_page)
    else:
        print('La requête n a pas aboutie.b')


scraping_page_category('http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html')
