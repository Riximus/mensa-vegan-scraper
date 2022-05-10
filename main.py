import requests
from bs4 import BeautifulSoup
from datetime import datetime as date

URL = "https://technolino.sv-restaurant.ch/de/menuplan/"

page = requests.get(URL)

# parse the content of the page
soup = BeautifulSoup(page.content, 'html.parser')

# get the content of the id
results = soup.find(id='menu-plan-tab4')

today = date.today().strftime("%A")

match today:
    case 'Monday':
        print(today)
    case 'Tuesday':
        print(today)
    case _:
        print("Today is not Monday or Tuesday")



#print(results.prettify())

menu_items = results.find_all(class_='menu-item')

for menu_item in menu_items:
    print(menu_item.text.strip())


#vegans = menu_plan.find_all(class_='label-vegan')
#print(vegans)

