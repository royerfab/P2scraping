import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'http://books.toscrape.com/catalogue/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html'

def image_url(image_url_relative):
    image_url_base = 'http://books.toscrape.com/'
    return image_url_base + image_url_relative.replace('../', '')

def download_image(image_url, title):
    f = open(title + ".jpg", 'wb')
    f.write(urllib.request.urlopen(image_url).read())
    f.close()


response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    conteneur_td = soup.find("table", class_="table table-striped")
    td = conteneur_td.find_all("td")
    product_page_url = url
    universal_product_code = td[0].text
    #title_incorrect = soup.find("h1").text
    title = soup.find("h1").text
    image_url_relative = soup.find("div", class_="item active").find("img").get('src')
    url_image = image_url(image_url_relative)
    download_image(url_image, title)

print(title)