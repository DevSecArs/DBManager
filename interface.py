from api import CRUD, DataBaseManager
        
def menu():
    print("""
===========================================
| Выберите действие:                      |
|    1. Создать БД                        |
|    2. Список БД                         |
|    3. Удалить БД                        |
|    4. Выбрать БД                        |
|    5. Выйти                             |        
===========================================
    """)

def greetings():
    print("""
===========================================
| Добро пожаловать в менеджер баз данных! |""", end="")
    menu()

def line():
    print("===========================================")

if __name__ == "__main__":
    # Приветствие
    greetings()

    dbm = DataBaseManager()
    while (True):
        match (int(input("Ваш выбор: "))):
            case 1:
                # Создать БД
                name = input("Введите название: ")
                print(f"[{name}] успешно создана!") if (dbm.create(name)) else print(f"[{name}] уже существует!")
            case 2:
                # Вывести список БД
                dbm.read()
            case 3:
                # Удалить БД
                dbm.read()
                name = input("Введите название: ")
                if (input(f"Вы точно хотите удалить [{name}]? (Y/n): ").lower() == "y"):
                    if (dbm.delete(name)): print(f"[{name}] успешно удалена.")
                    else: print("Неверное имя базы данных!")
            case 4:
                # Выбрать БД
                dbm.read()
                name = input("Введите название: ")
                if (dbm.exists(name)):
                    cursor = CRUD("name")
                    # match case CRUD
                else:
                    print("Неверное имя базы данных!")
            
            # Выход и обработка неверного ввода
            case 5:
                break
            case _:
                pass
        line()
