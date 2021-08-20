from bs4 import BeautifulSoup
import requests
import os
import csv
from scraping import scraping_one_product


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


#Fonction étendant le scraping des informations des produits à toutes les pages de la catégorie
def scraping_all_category(url):
    response = requests.get(url)
    list_product_category = []
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        page = soup.find("li", class_="current")
        if page != None:
            pagination = soup.find("li", class_="current").text
            divided = pagination.split(" ")
            page_number = int(divided[31])
            i=1
            while i <= page_number:
                page_url = url.replace('index.html', 'page-' + str(i) + '.html')
                i+=1
                response_2 = requests.get(page_url)
                if response_2.ok:
                    soup_2 = BeautifulSoup(response_2.content, 'html.parser')
                    products = soup_2.find_all("h3")
                    for product in products:
                        relative_link = product.find("a").get("href")
                        products_informations = scraping_one_product(book_url(relative_link))
                        list_product_category.append(products_informations)
                    print(list_product_category, 'dtu')
                else:
                    print('La requête n a pas abouti.')
            category_name = soup.find("h1").text
            create_csv(category_name, list_product_category)
        else:
            if response.ok:
                products = soup.find_all("h3")
                for product in products:
                    relative_link = product.find("a").get("href")
                    products_informations = scraping_one_product(book_url(relative_link))
                    list_product_category.append(products_informations)
                category_name = soup.find("h1").text
                create_csv(category_name, list_product_category)
            else:
                print('La requête n a pas abouti.a')
    else:
        print('La requête n a pas abouti.b')

