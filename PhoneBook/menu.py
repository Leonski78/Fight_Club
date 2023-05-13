from loader import book
from const import FILE_PATH


def start_menu():
    book.get_contact(FILE_PATH)
    print(book)