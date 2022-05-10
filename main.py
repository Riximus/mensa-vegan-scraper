import requests
from bs4 import BeautifulSoup

URL = "https://technolino.sv-restaurant.ch/de/menuplan/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="l-main")

print(results.prettify())


