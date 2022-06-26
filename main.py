

from ast import main
from pickle import FALSE
from typing import Dict
from unittest import result


def select():
    pass


def delete():
    pass


def update():
    pass


def insert():
    pass


def user_dialog():

    result_main = main_dialog()
    result_heroes = heroes_dialog(result_main)

    
        
       

        # elif p == 'Вернуться в предыдущее меню':
        #     return
        # elif p == 'Герои(Heroes)':
        #     name = input('\nВведите имя героя\n')
        # elif p == 'Доп.инфо(heroes_info)':
        #     name = input('\nВведите имя героя\n')
        # elif p == 'Характеристики(stats)':
        #     name = input('\nВведите имя героя\n')
        # elif p == 'Уровень меты(meta)':
        #     name = input('\nВведите имя героя\n')
        # elif p == None:
        #     print('Раздел меню не найден')


def get_main_menu():

    return {
        1: 'Получить данные',
        2: 'Добавить данные',
        3: 'Обновить данные',
        4: 'Удалить данные',
        0: 'Выйти из программы'
    }


def main_dialog():

    main_menu = get_main_menu()
    print_menu(main_menu)

    return input_process(main_menu)


def heroes_dialog(result_main):

    if result_main == '1':
        heroes_menu = get_heroes_menu()
        print_menu(heroes_menu)
        return input_process(heroes_menu)
    

def get_heroes_menu():

    return {
        1: 'Герои(Heroes)',
        2: 'Доп.инфо(heroes_info)',
        3: 'Характеристики(stats)',
        4: 'Уровень меты(meta)',
        9: 'Вернуться в предыдущее меню',
        0: 'Выйти из программы'
    }


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

def menu_exit():

    b = input('Хотите завершить работу с программой? (y/n)\n')
    if b == 'y':
        print('Вы вышли из программы')
        exit()
        
def menu_404():

     print('Раздел меню не найден')
     print('-----')


user_dialog()
