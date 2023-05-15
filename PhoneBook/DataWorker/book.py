from DataWorker import Contact
from const import FILE_PATH

class Book:
    def __init__(self, name: str = 'Телефонная книга', Phone_book: list = None):
        if Phone_book is None:
            Phone_book = []
        self.name = name
        self.Phone_book = Phone_book

    def add_contact(self, contact: Contact):
        self.Phone_book.append(contact)
        name = input('Введите имя: ')
        father = input('Введите отчество: ')
        surname = input('Введите фамилию: ')
        number = input('Введите номер телефона: ')
        with open(FILE_PATH, 'a', encoding='utf8') as Phone_book:
            Phone_book.write(f'\n{surname} {name} {father},{number}')

    def remove_contact(self, contact):
        self.Phone_book.remove(contact)
        with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
            all_phone_book = Phone_book.readlines()

    del_contact_data = input('Введите данные для удаления: ')
    result = [line for line in all_phone_book if del_contact_data not in line]

    with open(FILE_PATH, 'w', encoding='utf8') as Phone_book:
        for line in result:
            Phone_book.write(line)

    def get_contact(self, path):
        with open(path, 'r', encoding='utf8') as Phone_book:
            for line in Phone_book:
                line = line.strip().split(',')
                print(Contact(*line))

    def search_phone_book(self, contact):
        self.Phone_book.search(contact)
        with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
            search_data = input('Введите данные для поиска: ')
            for line in Phone_book:
                if search_data in line:
                    print(line.strip())

