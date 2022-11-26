from typing import Dict
from actions import *
from menu_items import *
from operations import initial_db, select_db, insert_db, update_db, delete_db
from db.create import get_engine, get_meta

engine = get_engine()
meta = get_meta(engine)
con = engine.connect()


def user_dialog():
    # initial_db()
    result_main = main_dialog()
    result_heroes = heroes_dialog(result_main)
    heroes_dialog_operations(result_heroes, result_main)


def heroes_dialog_operations(id, operation='1'):
    if operation == '9':
        user_dialog()
    elif operation == '0':
        menu_exit(user_dialog)
    else:

        response = {}
        # select
        if operation == '1':
            response = select_db(operation, id, con, meta)

        # insert
        if operation == '2':
            response = insert_db(operation, id, con, meta)

        if operation == '3':
            response = update_db(operation, id, con, meta)

        if operation == '4':
            response = delete_db(operation, id, con, meta)

        print(response)

    user_dialog()


def main_dialog():
    main_menu = get_main_menu()
    print_menu(main_menu)

    return input_process(main_menu, user_dialog)


def heroes_dialog(result_main='1'):
    if result_main == '1' or result_main == '2':
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
