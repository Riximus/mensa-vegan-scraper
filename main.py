import requests
from bs4 import BeautifulSoup
from datetime import datetime as date

URL = "https://technolino.sv-restaurant.ch/de/menuplan/"


# get the content of the id

# TODO check if today is a week day or only search for a menu if its weekday or only send a request on Monday/Tuesday
def today_menu(menus):
    # today = date.today().strftime("%A")
    today = 'Monday'
    match today:
        case 'Monday':
            check_menu_type(menus)
        case 'Tuesday':
            print(today)
        case _:
            print("Today is not Monday or Tuesday")


def check_menu_type(menus):
    if type(menus) == str:
        print(menus)
    else:
        for menu, desc in menus.items():
            print(menu)
            print(desc)


def get_soup():
    page = requests.get(URL)
    # parse the content of the page
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def find_vegan_menu(soup):
    menus_dict = {}
    no_vegan_str = 'The menus today are not vegan 😔'
    # get the first tab (that's usual today)
    results = soup.find(id='menu-plan-tab1')

    menu_items = results.find_all(class_='menu-item')
    for menu_item in menu_items:
        vegan = menu_item.find_next(class_='item-content').find(class_='label-info label-vegan')
        if vegan is not None:
            menu_name = menu_item.find_next(class_='menu-title')
            menu_desc = menu_item.find_next(class_='menu-description')

            # fill dictionary with menu name and description
            menus_dict[menu_name.text.strip()] = menu_desc.text.strip()

    # if dictionary empty
    if not menus_dict:
        return no_vegan_str

    return menus_dict


def main():
    menus = find_vegan_menu(get_soup())
    today_menu(menus)


if __name__ == '__main__':
    main()
