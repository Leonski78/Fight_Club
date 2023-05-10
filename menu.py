import data_worker 

def start_menu():
    while True:
        change = int(input('\n1. Посмотреть всю книгу'
                        '\n2. Найти контакт'
                        '\n3. Удалить контакт'
                        '\n4. Добавить контакт'
                        '\n5 Выйти'
                        '\n--> '))
        # if change == 1:
        #     data_worker.get_phone_book()
        # elif change == 2:
        #     data_worker.search_phone_book()
        # elif change == 3:
        #     data_worker.del_contact()
        # elif change == 4:
        #     data_worker.add_contact()
        # else:
        #     break
        match change:
            case 1:
                data_worker.get_phone_book()
            case 2:
                data_worker.search_phone_book()
            case 3:
                data_worker.del_contact()
            case 4:
                data_worker.add_contact()
            case _:
                break





