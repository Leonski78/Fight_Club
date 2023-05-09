from const import FILE_PATH

def del_contact():
    with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
        all_phone_book = Phone_book.readlines()

    del_contact_data = input('Введите данные для поиска: ')
    result = [line for line in all_phone_book if del_contact_data not in line]

    with open(FILE_PATH, 'w', encoding='utf8') as Phone_book:
        for line in result:
            Phone_book.write(line)

def add_contact():
    name = input('Введите имя: ')
    father = input('Введите отчество: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер телефона: ')
    with open(FILE_PATH, 'a', encoding='utf8') as Phone_book:
        Phone_book.write(f'\n{surname} {name} {father},{number}')