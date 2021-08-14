from bs4 import BeautifulSoup
import requests

url ='http://books.toscrape.com/catalogue/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares-star-wars-4_871/index.html'
response = requests.get(url)

def image_url(image_url_relative):
    image_url_base = 'http://books.toscrape.com/'
    return image_url_base + image_url_relative.replace('../', '')

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
        number_available = td[5].text
        conteneur_p = soup.find("article", class_='product_page')
        p_description = conteneur_p.find_all("p")
        product_description = p_description[3].text
        conteneur_a_category = soup.find("ul", class_='breadcrumb')
        a_category = conteneur_a_category.find_all("a")
        category = a_category[2].text
        review_rating_origin = str(soup.find("p", class_="star-rating"))
        review_rating_2 = review_rating_origin[22: 27]
        if review_rating_2 == 'One">':
            review_rating_2 = 'Une'
        elif review_rating_2 == 'Two">':
            review_rating_2 = 'Deux'
        elif review_rating_2 == 'Three':
            review_rating_2 = 'Trois'
        elif review_rating_2 == 'Four"':
            review_rating_2 = 'Quatre'
        elif review_rating_2 == 'Five"':
            review_rating_2 = 'Cinq'
        if review_rating_2 == 'Une':
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
        return product_informations
    else:
        return {}
scraping_one_product('http://books.toscrape.com/catalogue/william-shakespeares-star-wars-verily-a-new-hope-william-shakespeares-star-wars-4_871/index.html')