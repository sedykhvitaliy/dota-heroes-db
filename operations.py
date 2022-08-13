import csv
from menu_items import get_database

DB_HEADERS = {}


def select(file_name: str, field_name: str, field_search: str):

    with open(file_name, "r", encoding="UTF-8") as file:
        bd = csv.DictReader(file, delimiter=';')
        for line in bd:
            if field_search.lower() == line[field_name].lower():
                return line
                break
    return {}


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