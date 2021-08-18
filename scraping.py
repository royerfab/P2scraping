from bs4 import BeautifulSoup
import requests
import csv
import os


os.mkdir('C:/Users/julie/PycharmProjects/pythonProject/Fichier_CSV')
url ='http://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html'
response = requests.get(url)


#fonction intégrant dans un fichier csv les données recueillies
def create_csv(category, product_informations):
    os.chdir('C:/Users/julie/PycharmProjects/pythonProject/Fichier_CSV')
    with open(category + '.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=['product_page_url', 'universal_product_code',
                                               'title', 'prices_including_taxes',
                                               'prices_excluding_taxes', 'number_available',
                                               'product_description', 'category',
                                               'review_rating', 'image_url'])
        writer.writeheader()
        writer.writerow(product_informations)


#fonction reconstituant l'url de l'image à partir d'une url relative
def image_url(image_url_relative):
    image_url_base = 'http://books.toscrape.com/'
    return image_url_base + image_url_relative.replace('../', '')


#Fonction extrayant les informations d'une page produit avec BeautifulSoup, regroupées dans un dictionnaire
def scraping_one_product(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        conteneur_td = soup.find("table", class_="table table-striped")
        td = conteneur_td.find_all("td")
        product_page_url = url
        universal_product_code = td[0].text
        title = soup.find("h1").text
        prices_including_taxes = td[3].text
        prices_excluding_taxes = td[2].text
        number = td[5].text
        number_available = number[10:12]
        conteneur_p = soup.find("article", class_='product_page')
        p_description = conteneur_p.find_all("p")
        product_description = p_description[3].text
        conteneur_a_category = soup.find("ul", class_='breadcrumb')
        a_category = conteneur_a_category.find_all("a")
        category = a_category[2].text
        review_rating_origin = str(soup.find("p", class_="star-rating"))
        review_rating_2 = review_rating_origin[22: 27]
        if review_rating_2 == 'One">':
            review_rating_2 = '1'
        elif review_rating_2 == 'Two">':
            review_rating_2 = '2'
        elif review_rating_2 == 'Three':
            review_rating_2 = '3'
        elif review_rating_2 == 'Four"':
            review_rating_2 = '4'
        elif review_rating_2 == 'Five"':
            review_rating_2 = '5'
        if review_rating_2 == '1':
            review_rating = review_rating_2 + ' étoile'
        else:
            review_rating = review_rating_2 + ' étoiles'
        image_url_relative = soup.find("div", class_="item active").find("img").get('src')
        url_image = image_url(image_url_relative)
        product_informations = {'product_page_url': product_page_url, 'universal_product_code': universal_product_code,
                                'title': title, 'prices_including_taxes': prices_including_taxes,
                                'prices_excluding_taxes': prices_excluding_taxes, 'number_available': number_available,
                                'product_description': product_description, 'category': category,
                                'review_rating': review_rating, 'image_url': url_image}
        print(product_informations)
        create_csv(category, product_informations)
        return product_informations
    else:
        return {}


scraping_one_product('http://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html')