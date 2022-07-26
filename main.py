from typing import Dict
from actions import *
from menu_items import *
from operations import select


def user_dialog():

    result_main = main_dialog()
    result_heroes = heroes_dialog(result_main)
    heroes_dialog_operations(result_heroes)


def heroes_dialog_operations(id):
    #key_database = input('Введите желаемую баззу данных ')
    #database =  get_database.get(key_database, default = None)
    
    if id == '1':
        name = input("Введите имя, которое хотите найти\n")
        data = select("bd\heroes.csv", "name", name)
        print(select('bd\heroes.csv', "name", data.get('name')))
    
    elif id == '2':
        
        name = input("Введите имя, которое хотите найти\n")

        data = select("bd\heroes.csv", "name", name)

        print(select("bd\heroes_info.csv", "id", data.get('id')))

    elif id == '3':
        id = input("Введите имя, которое хотите найти\n")
        data = select("bd\heroes.csv", "name", name)
        print(select("bd\stats.csv", "id", data.get('id')))
    elif id == '4':
        id = input("Введите имя, которое хотите найти\n")
        data = select("bd\heroes.csv", "name", name)
        print(select("bd\meta.csv", "id", data.get('id')))
    elif id == '9':
        user_dialog()
    elif id == '0':
        menu_exit(user_dialog)
    else:
        menu_404()

    user_dialog()


def main_dialog():

    main_menu = get_main_menu()
    print_menu(main_menu)

    return input_process(main_menu, user_dialog)


def heroes_dialog(result_main='1'):

    if result_main == '1':
        heroes_menu = get_heroes_menu()
        print_menu(heroes_menu)
        return input_process(heroes_menu, heroes_dialog)


def print_menu(menu: Dict):

    for key, value in menu.items():
        print(key, ' - ', value)
    print('-----')


def input_process(menu: Dict, return_dialog):

    result = input('Введите ключ, что хотите получить\n')
    if result.isdecimal() == False:
        menu_404()
        return input_process(menu, return_dialog)

    current = menu.get(int(result))

    if result == '0':
        result = menu_exit(return_dialog)

    elif current == None:

        menu_404()
        main_dialog()

    return result


if __name__ == "__main__":
    user_dialog()
