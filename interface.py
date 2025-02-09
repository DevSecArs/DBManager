from api import CRUD, DataBaseManager
        
def dbm_menu():
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
    dbm_menu()

def line():
    print("===========================================")

def crud_menu(db:str):
    print(f"""
===========================================
| Выберите действие [{db}]:               |
|    1. Добавить запись                   |
|    2. Просмотреть записи                |
|    3. Изменить запись                   |
|    4. Удалить запись                    |
|    5. Вернуться                         |        
===========================================
    """)
    cursor = CRUD(db)
    while True:
        match (input("Ваш выбор: ")):
            case '1':
                data = input("Введите данные через | (имя|возраст|и т.д.):\n").strip()
                cursor.create(data)
                print("Запись добавлена.")
            case '2': 
                cursor.read()
            case '3': 
                try:
                    id = int(input("Введите id: "))
                except ValueError:
                    print("[Ошибка] id должен быть числом!")
                    continue
                if (cursor.update(id, input("Введите новые данные через |:\n"))): print("Данные успешно изменены.")
                else: print("[Ошибка] записи с указанным id не существует!")
            case '4': 
                try:
                    id = int(input("Введите id: "))
                except ValueError:
                    print("[Ошибка] id должен быть числом!")
                    continue
                if (cursor.delete(id)): print("Запись успешно удалена.")
                else: print("[Ошибка] записи с указанным id не существует!")

            case '5': break
            case _: print("Неверное значение")

if __name__ == "__main__":
    # Приветствие
    greetings()

    dbm = DataBaseManager()
    while True:
        match (input("Ваш выбор: ")):
            case '1':
                # Создать БД
                name = input("Введите название: ")
                print(f"[{name}] успешно создана!") if (dbm.create(name)) else print(f"[{name}] уже существует!")
            case '2':
                # Вывести список БД
                dbm.read()
            case '3':
                # Удалить БД
                dbm.read()
                name = input("Введите название: ")
                if (input(f"Вы точно хотите удалить [{name}]? (Y/n): ").lower() == "y"):
                    if (dbm.delete(name)): print(f"[{name}] успешно удалена.")
                    else: print("[Ошибка] Неверное имя базы данных!")
                else: print("Отмена.")
            case '4':
                # Выбрать БД
                dbm.read()
                name = input("Введите название: ")
                if (dbm.exists(name)):
                    crud_menu(name)
                else:
                    print("[Ошибка] Неверное имя базы данных!")
            
            # Выход и обработка неверного ввода
            case '5':
                print("Выход...")
                break
            case _: print("Неверное значение")
        line()
