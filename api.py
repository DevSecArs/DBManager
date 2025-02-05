""" Класс для работы с данными внутри базы данных """
class CRUD:
    def __init__(self, db:str):
        self.db = db

    def get_last_id(self):
        pass
    
        
    # ========== Основа ============ #

    def create(self, data:str):
        pass

    def read(self, id:int = -1):
        pass

    def update(self, id:int, new_line:str):
        pass

    def delete(self, id:int):
        pass


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


