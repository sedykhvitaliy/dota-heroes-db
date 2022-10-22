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


def get_table_from_operation(operation, meta):
    table = None
    if operation == '1':
        table = Heroes.__tablename__
    if operation == '2':
        table = Stats.__tablename__
    if operation == '3':
        table = Heroes_info.__tablename__

    if table is not None:
        table = Table(table, meta, autoload=True)

    return table


def select_db(operation, con, meta):
    table = get_table_from_operation(operation, meta)
    insert_heroes_name = input('Введите имя персонажа')
    select_heroes_information = table.select().where(table.c.name == insert_heroes_name)
    result = con.execute(select_heroes_information)
    return {'data': result.first()}


def delete():
    pass


def update():
    pass


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
