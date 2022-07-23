def menu_exit(return_dialog):

    result = input('Хотите завершить работу с программой? (y/n)\n')
    if result == 'y':
        print('Вы вышли из программы')
        exit()
    elif result == 'n':
        return return_dialog()
    else:
        menu_exit(return_dialog)


def menu_404():

    print('Раздел меню не найден')
    print('-----')
