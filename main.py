from html.entities import name2codepoint


def select():
    pass


def delete():
    pass


def update():
    pass


def insert():
    pass


def user_dialog():

    a = {1: 'Получить данные', 2: 'Добавить данные', 3: 'Обновить данные', 4: 'Удалить данные', 0: 'Выйти из программы'}
    for key, value in a.items():
            print(key, value)
    i = int(input('Введите ключ, что хотите получить\n'))
    n = a.get(i)
    print(n)
    if n == 'Выйти из программы':
            b = input('Хотите завершить работу с программой? (y/n)\n')
            if b == 'y':
                print('Вы вышли из программы')
                exit()
    elif n == None:
             print('Раздел меню не найден')

    elif n == 'Получить данные':
        c = {1:'Герои(Heroes)', 2:'Доп.инфо(heroes_info)', 3:'Характеристики(stats)', 4:'Уровень меты(meta)', 9:'Вернуться в предыдущее меню', 0:'Выйти из программы'}     
        for key, value in c.items():
            print(key, value)
        
        
        r = int(input('Введите ключ, что хотите получить\n'))
        p = c.get(r)
        print(n)
        b = input('Хотите завершить работу с программой? (y/n)\n')
        if b == 'y':
            if n == 'Выйти из программы':
                print('Вы вышли из программы')
                exit()

        elif c == 9:
            print()
        elif c == 1:
            name = input('\nВведите имя героя\n')
        elif c == 2:
            name = input('\nВведите имя героя\n')
        elif c == 3:
            name = input('\nВведите имя героя\n')
        elif c == 4:
            name = input('\nВведите имя героя\n')


user_dialog()
