from DataWorker import Contact

class Book:
    def __init__(self, name: str = 'Телефонная книга', Phone_book: list = None):
        if Phone_book is None:
            Phone_book = []
        self.name = name
        self.Phone_book = Phone_book

    def add_contact(self, contact: Contact):
        self.Phone_book.append(contact)

    def remove_contact(self, contact):
        self.Phone_book.remove(contact)

    def get_contact(self, path):
        with open(path, 'r', encoding='utf8') as Phone_book:
            for line in Phone_book:
                line = line.strip().split(',')
                print(Contact(*line))


