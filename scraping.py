from bs4 import BeautifulSoup
import requests
import os
import urllib.request


os.mkdir('C:/Users/julie/PycharmProjects/pythonProject/Images')
os.mkdir('C:/Users/julie/PycharmProjects/pythonProject/Fichier_CSV')


#Fonction reconstituant l'url de l'image à partir d'une url relative
def image_url(image_url_relative):
    image_url_base = 'http://books.toscrape.com/'
    return image_url_base + image_url_relative.replace('../', '')


#Fonction corrigeant l'écriture des titres des produits
def replaceMultiple(incorrect_title, toBeReplaces, newString):
    for element in toBeReplaces:
        if element in incorrect_title:
            incorrect_title = incorrect_title.replace(element, newString)
    return incorrect_title


#Fonction téléchargeant l'image de chaque produit au sein d'une dossier
def download_image(image_url, title):
    os.chdir('C:/Users/julie/PycharmProjects/pythonProject/Images')
    f = open(title + ".jpg", 'wb')
    f.write(urllib.request.urlopen(image_url).read())
    f.close()


#Fonction extrayant les informations d'une page produit avec BeautifulSoup, regroupées dans un dictionnaire
def scraping_one_product(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        conteneur_td = soup.find("table", class_="table table-striped")
        td = conteneur_td.find_all("td")
        product_page_url = url
        universal_product_code = td[0].text
        incorrect_title = soup.find("h1").text
        title = replaceMultiple(incorrect_title, [':', '/', ';', '*', '"','>', '?'], '')
        prices_including_taxes = td[3].text
        prices_excluding_taxes = td[2].text
        number = td[5].text
        number_available = replaceMultiple(number, ['In stock (', 'available)'], '')
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
        download_image(url_image, title)
        return product_informations
    else:
        return {}