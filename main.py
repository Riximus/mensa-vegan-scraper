import requests
from bs4 import BeautifulSoup
from datetime import datetime as date
from plyer import notification

URL = "https://technolino.sv-restaurant.ch/de/menuplan/"
error = 'error'
noti_title = 'MENSA HEUTE 🍴'
show_time = 15


def today_menu(menus):
    today = date.today().strftime("%A")

    if menus == error:
        return 'There is nothing in this week / Can be an error'
    elif today == 'Monday' or today == 'Tuesday':
        if isinstance(menus, dict):
            for menu, desc in menus.items():
                return '🌻' + menu + '🌻' + '\n' + desc
        else:
            return menus
    else:
        return 'Today is not Monday or Tuesday'


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

    # error handle if menu-plan-tab1 exists
    try:
        menu_items = results.find_all(class_='menu-item')
    except AttributeError:
        return error

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
    noti_message = today_menu(menus)

    notification.notify(
        title=noti_title,
        message=noti_message,
        timeout=show_time
    )


if __name__ == '__main__':
    main()
