import requests
from bs4 import BeautifulSoup

URL = "https://technolino.sv-restaurant.ch/de/menuplan/"

page = requests.get(URL)

# parse the content of the page
soup = BeautifulSoup(page.content, "html.parser")

# get the content of the id
results = soup.find(id="l-main")

#print(results.prettify())

# returns all days in the "banner"
days = results.find("ul", class_="no-bullets is-horizontal")
#print(days)
span_days = days.find_all("span", class_="day")

print(span_days[0].text.strip())

menus = results.find("div", id="menu-plan-tab1")

print(menus.prettify())
