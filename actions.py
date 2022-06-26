def menu_exit():

    result = input('Хотите завершить работу с программой? (y/n)\n')
    if result == 'y':
        print('Вы вышли из программы')
        exit()


def menu_404():

    print('Раздел меню не найден')
    print('-----')
