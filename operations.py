import csv


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
    with open(file_name, "r", encoding="UTF-8") as file:
        bd = csv.reader(file, delimiter=';')
        for line in bd:
            i = 0
            while i < len(line):
                print('Введите что запрашивают')
                user_input = input(line[i])
                i += 1
            line_dictionary = dict.fromkeys(line, user_input)  
            print(line_dictionary)
            break


    return {}
