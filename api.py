from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

""" Класс для работы с данными внутри базы данных """
class CRUD:
    def __init__(self, db:str):
        self.db = db

    @staticmethod
    def replace(file_path, old_line, new_line):
        # Создаём временный файл, в который вносим изменения
        temp, temp_path = mkstemp()
        with fdopen(temp, 'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(old_line, new_line))
        # Копируем права доступа
        copymode(file_path, temp_path)
        # Удаляем старый файл
        remove(file_path)
        # Перемещаем новый файл
        move(temp_path, file_path)

    def get_last_id(self):
        with open(f"{self.db}.txt", "r", encoding="utf-8") as file:
            try:
                data = file.readlines()[-1]
            except IndexError:
                return -1
            last_id = int(data.split("|")[0])
        return last_id
    
    def get_line(self, id:int):
        with open(f"{self.db}.txt", "r", encoding="utf-8") as file:
            line = "".join([str(line) for line in file.readlines() if str(id) in line.split("|")[0]])
            return line
        
    # ========== Основа ============ #

    def create(self, data:str):
        with open(f"{self.db}.txt", "a", encoding="utf-8") as file:
            new_id = self.get_last_id() + 1
            file.write(f"{new_id}|{data}\n")

    def read(self, id:int = -1):
        with open(f"{self.db}.txt", "r", encoding="utf-8") as file:
            if (id < 0):
                [print(line, end="") for line in file.readlines()]
            else:
                [print(line, end="") for line in file.readlines() if str(id) in line.split("|")[0]]

    def update(self, id:int, new_line:str):
        old_line = self.get_line(id)
        self.replace(f"{self.db}.txt", old_line, f"{id}|{new_line}\n")

    def delete(self, id:int):
        old_line = self.get_line(id)
        self.replace(f"{self.db}.txt", f"{old_line}", "")


""" Класс для управления базами данных """
class DataBaseManager:
    
    """ Создание текстовой базы данных """
    @staticmethod
    def create(name:str):
        pass

    """ Показ существующих баз данных и их структуры """
    @staticmethod
    def read():
        pass

    """ Обновление структуры базы данных """
    @staticmethod
    def update():
        pass

    """ Удаленние базы данных """
    @staticmethod
    def delete(name):
        pass


