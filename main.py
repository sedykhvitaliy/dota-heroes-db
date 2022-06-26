from typing import Dict
from actions import *
from menu_items import *


def user_dialog():

    result_main = main_dialog()
    result_heroes = heroes_dialog(result_main)


def main_dialog():

    main_menu = get_main_menu()
    print_menu(main_menu)

    return input_process(main_menu)


def heroes_dialog(result_main):

    if result_main == '1':
        heroes_menu = get_heroes_menu()
        print_menu(heroes_menu)
        return input_process(heroes_menu)


def print_menu(menu: Dict):

    for key, value in menu.items():
        print(key, ' - ', value)
    print('-----')


def input_process(menu: Dict):

    result = input('Введите ключ, что хотите получить\n')
    if result.isdecimal() == False:
        menu_404()
        return input_process(menu)

    current = menu.get(int(result))

    if result == '0':
        menu_exit()

    elif current == None:
        menu_404()
        main_dialog()

    return result


if __name__ == "__main__":
    user_dialog()
