class Contact:
    def __init__(self, surname, name, father, number):
        self.surname = surname
        self.name = name
        self.father = father
        self.number = number

    def change_name(self, new_name):
        self.name = new_name
        
    def __str__(self):
        return f'Фамилия: {self.surname}    Имя: {self.name}    Отчество: {self.father}    телефон: {self.number}'
    
      