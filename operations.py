import csv

from db.models import Heroes, Stats, Heroes_info
from menu_items import get_database
from sqlalchemy import Table

DB_HEADERS = {}


def select(file_name: str, field_name: str, field_search: str):
    with open(file_name, "r", encoding="UTF-8") as file:
        bd = csv.DictReader(file, delimiter=';')
        for line in bd:
            if field_search.lower() == line[field_name].lower():
                return line
                break
    return {}


def get_table_from_id(id, meta):
    table = None
    if id == '1':
        table = Heroes.__tablename__
    if id == '2':
        table = Stats.__tablename__
    if id == '3':
        table = Heroes_info.__tablename__

    if table is not None:
        table = Table(table, meta, autoload=True)

    return table


def select_db(operation, table_id, con, meta):
    table = get_table_from_id(table_id, meta)
    select_heroes_information = None
    data = {}
    if operation == '1':
        insert_heroes_name = input('Введите имя персонажа: \n')
        select_heroes_information = table.select().where(table.c.name == insert_heroes_name)

    if operation == '2' or operation == '3':
        insert_heroes_id = input('Введите id персонажа: \n')
        select_heroes_information = table.select().where(table.c.id == insert_heroes_id)

    if select_heroes_information is not None:
        result = con.execute(select_heroes_information)
        data = {'data': result.first()}

    return data


def delete_db(operation, table_id, con, meta):
    table = get_table_from_id('1', meta)
    select_heroes_information = table.select()
    result = con.execute(select_heroes_information)
    count = 1
    heroes_data = {}
    for row in result.fetchall():
        print(f'{count} - {row[1]}')
        heroes_data[count] = row
        count += 1
    user_input_number = int(input('Выберите номер героя: '))
    print(heroes_data[user_input_number])
    id_heroes = heroes_data[user_input_number][0]
    delete_sub_table(id_heroes, con, meta, '2')
    delete_sub_table(id_heroes, con, meta, '3')
    delete_main_heroes_information = table.delete().where(table.c.id_heroes == id_heroes)
    con.execute(delete_main_heroes_information)
    return 'done'


def delete_sub_table(id_heroes, con, meta, table_id):
    table = get_table_from_id(table_id, meta)
    select_heroes_info = table.select().where(table.c.heroes_id == id_heroes)
    result = con.execute(select_heroes_info)
    print(result.first())
    if select_heroes_info is not None:
        delete_heroes_information = table.delete().where(table.c.heroes_id == id_heroes)
        result = con.execute(delete_heroes_information)


def update_db(operation, table_id, con, meta):
    table = get_table_from_id('1', meta)
    select_heroes_information = table.select()
    result = con.execute(select_heroes_information)
    count = 1
    heroes_data = {}
    for row in result.fetchall():
        print(f'{count} - {row[1]}')
        heroes_data[count] = row
        count += 1
    user_input_number = int(input('Выберите номер героя: '))
    print(heroes_data[user_input_number])
    id_heroes = heroes_data[user_input_number][0]
    data = {}
    count = 1
    column_dict = {}
    for column in table.c:
        if not (column.primary_key or len(column.foreign_keys) > 0):
            column_dict[count] = column.name
            count += 1
    print("Доступные колонки для изменения:")
    for i in column_dict:
        print(f'{i} - {column_dict[i]}')

    user_input_column = int(input('Выберите номер колонки: '))

    user_input = int(input(f'Введите {column_dict[user_input_column]}: '))
    data[column.name] = user_input
    update_heroes_information = table.update().where(table.c.id_heroes == id_heroes).values(data)
    con.execute(update_heroes_information)


def insert(file_name: str):
    headers = DB_HEADERS.get(file_name)

    with open(file_name, "a", encoding="UTF-8", newline='') as file:

        i = 1
        line_dictionary = dict.fromkeys(headers)
        while i < len(headers):

            print(f'Введите {headers[i]}:')
            user_input = input()
            if user_input.strip():
                line_dictionary[headers[0]] = get_last_id(file_name) + 1
                line_dictionary[headers[i]] = user_input.strip()
                i += 1
            else:
                print('Введите ещё раз')
        dictwriter_object = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        dictwriter_object.writerow(line_dictionary)
        file.close()

    return print(f'Добавлена запись: {line_dictionary}')


def insert_db(operation, table_id, con, meta):
    table = get_table_from_id(table_id, meta)
    select_heroes_information = None
    data = {}
    if operation == '2':

        data = {}
        for column in table.c:
            if not (column.primary_key or len(column.foreign_keys) > 0):
                user_input = input(f'Введите {column.name}:')
                data[column.name] = user_input
                # заполняем словарь введенными данными

        select_heroes_information = table.insert().values(data)

    if select_heroes_information is not None:
        con.execute(select_heroes_information)
        data = {'data': data}

    return data


def initial_db():
    database = get_database()
    headers = []
    for id in database:
        table = database.get(int(id))
        with open(table, "r", encoding="UTF-8") as file:
            bd = csv.reader(file, delimiter=';')
            for line in bd:
                headers = line
                break
            DB_HEADERS[table] = headers
            file.close()


def get_last_id(file_name):
    last_id = 0
    with open(file_name, "r", encoding="UTF-8") as file:
        bd = csv.DictReader(file, delimiter=';')
        all_lines = list(bd)
        last_line = (all_lines[-1])
        last_id = int(last_line['id'])

    return last_id
