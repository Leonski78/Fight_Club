from const import FILE_PATH

def get_phone_book():
    with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
        for line in Phone_book:
            print(line.strip())

def search_phone_book():
    with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
        search_data = input('Введите данные для поиска: ')
        for line in Phone_book:
            if search_data in line:
                print(line.strip())
