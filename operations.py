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
   
    headers = []
    with open(file_name, "r", encoding="UTF-8") as file:
        bd = csv.reader(file, delimiter=';')
        for line in bd:
            headers = line
            break
        file.close()

    with open(file_name, "a", encoding="UTF-8", newline='') as file:
    
        i = 0
        line_dictionary = dict.fromkeys(headers)  
        while i < len(headers):
            print(f'Введите {headers[i]}:')
            user_input = input()
            line_dictionary[headers[i]] = user_input.strip()
            i += 1

        dictwriter_object = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        dictwriter_object.writerow(line_dictionary)
        file.close()


    return print(f'Добавлена запись: {line_dictionary}')
