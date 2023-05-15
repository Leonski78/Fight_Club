from const import FILE_PATH

class Contact:
    def __init__(self, surname, name, father, number):
        self.surname = surname
        self.name = name
        self.father = father
        self.number = number

    def change_name(self, new_name):
        self.name = new_name
        with open(FILE_PATH, 'r', encoding='utf8') as Phone_book:
            change_phone_book = Phone_book.readlines()
        change_contact_data = input('Введите данные для изменения: ')

        for i in range(len(change_phone_book)):
            if change_contact_data in change_phone_book[i]:
                if i != len(change_phone_book) - 1:
                    change_phone_book[i] = input('Введите новые данные: ') + '\n'
                else:
                    change_phone_book[i] = input('Введите новые данные: ')
                break

        with open(FILE_PATH, 'w', encoding='utf8') as Phone_book:
            for line in change_phone_book:
                Phone_book.write(line)    
        
    def __str__(self):
        return f'Фамилия: {self.surname}    Имя: {self.name}    Отчество: {self.father}    телефон: {self.number}'
    
