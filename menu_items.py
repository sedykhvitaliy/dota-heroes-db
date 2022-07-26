def get_main_menu():

    return {
        1: 'Получить данные',
        2: 'Добавить данные',
        3: 'Обновить данные',
        4: 'Удалить данные',
        0: 'Выйти из программы'
    }


def get_heroes_menu():

    return {
        1: 'Герои(Heroes)',
        2: 'Доп.инфо(heroes_info)',
        3: 'Характеристики(stats)',
        4: 'Уровень меты(meta)',
        9: 'Вернуться в предыдущее меню',
        0: 'Выйти из программы'
    }


def get_database():
    return {
        1: 'bd\heroes.csv',
        2: 'bd\heroes_info.csv',
        3: 'bd\meta.csv',
        4: 'bd\stats.csv',

    }
