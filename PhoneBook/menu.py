from loader import book
# from loader import contact
from const import FILE_PATH


def start_menu():
    book.get_contact(FILE_PATH)
    print(book)
    change = int(input('\n1. Посмотреть всю книгу'
                        '\n2. Найти контакт'
                        '\n3. Удалить контакт'
                        '\n4. Добавить контакт'
                        '\n5. Изменить контакт'
                        '\n6 Выйти'
                        '\n--> '))
    match change:
        case 1:
            book.get_contact()
        case 2:
            book.search_phone_book()
        case 3:
            book.remove_contact()
        case 4:
            book.add_contact()
        case 5:
            contact.change_name()
        case _:
            # break
            exit()

