def select():
    pass

def delete():
    pass

def update():
    pass

def insert():
    pass

def user_dialog():
    
    a = int(input('Выберите что вы хотите сделать:\n1.Получить данные\n2.Добавить данные\n3.Обновить данные\n4.Удалить данные\n0.Выйти из программы\n'))
    while True:
        if a == 0:
            b = input('Вы уверенны?\n')
            if b == 'Да':
                print('Вы вышли из программы')
                break
        elif a>4:
            break
        elif a<4:
            c = int(input('\n1.Герои(Heroes)\n2.Доп.инфо(heroes_info\n3.Характеристики(stats)\n4.Уровень меты(meta)\n9.Вернуться в предыдущее меню\n0.Выйти из программы\n'))
            if c == 0:
                break
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