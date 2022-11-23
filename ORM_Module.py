import sqlite3


class OrmModel():
    def __init__(self):
        """Инициализация атрибутов"""
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"CREATE TABLE IF NOT EXISTS ORMModelTable(id INT PRIMARY KEY)")

    # Метод создания поля. переопределен в классах
    def create_value(self):
        """Создание поля"""
        print("Невозможно создать поле. Метод дочернего класса недоступен")

    # Метод вставки значений в бд
    def insert_value(self, lst_column, lst_data):
        """Вставка данных в таблицу"""

        lst_data = tuple(lst_data)
        # Вспомогательный метод для подсчета и генерации вопросов для SQL запроса
        count = 0
        column = ""

        for item in lst_column:
            count += 1

        for i in range(0,count):
            column = column + "?, "

        column = column[:-2]

        lst_column = ", ".join(lst_column)


        
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"CREATE TABLE IF NOT EXISTS ORMModelTable(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")
        cursorObj = con.cursor()
        cursorObj.execute(f'INSERT INTO ORMModelTable({lst_column}) VALUES({column})', lst_data)
        con.commit()
        con.close()

    # Метод обновляет значение в бд по id
    def update_value(self, column_name, id, value):
        """Обновление таблицы"""
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"UPDATE ORMModelTable "
                          f"SET {column_name} = {value} WHERE id = {id}"
                          )
        con.commit()
        con.close()

    # Метод поиска по значению
    def filter_value(self, columns_for_show, column_for_search, value):
        """Поиск по колонке"""
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f'SELECT {columns_for_show} FROM ORMModelTable WHERE {column_for_search} = {value}')
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        con.close()

    def all_value(self):
        """Вывод всех значений"""
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute('SELECT * FROM ORMModelTable')
        rows = cursorObj.fetchall()
        for row in rows:
            print(row)
        con.close()

# Удаление таблицы
    def delete_value(self, table_name):
        """Удаление таблицы"""
        print(table_name)
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f'DROP table if exists {table_name}')
        con.commit()
        con.close()


class OrmText(OrmModel):
    def __init__(self):
        """Создание поля"""

# Метод создания текстового поля таблицы
    def create_value(self, value):
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"CREATE TABLE IF NOT EXISTS ORMModelTable(id INT PRIMARY KEY)")
        cursorObj.execute(f"ALTER TABLE ORMModelTable ADD '{value}' TEXT")
        con.commit()
        con.close()


class OrmInteger(OrmModel):
    def __init__(self):
        """Создание поля"""

# Метод создания числового поля таблицы
    def create_value(self, value):
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"CREATE TABLE IF NOT EXISTS ORMModelTable(id INT PRIMARY KEY)")
        cursorObj.execute(f"ALTER TABLE ORMModelTable ADD '{value}' INT")
        con.commit()
        con.close()


class OrmFloat(OrmModel):
    def __init__(self, value):
          """инициализирует атрибуты класса-родителя."""
          super().__init__(value)

    def create_value(self, value):
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        cursorObj.execute(f"CREATE TABLE IF NOT EXISTS ORMModelTable(id INT PRIMARY KEY)")
        cursorObj.execute(f"ALTER TABLE ORMModelTable ADD '{value}' FLOAT")
        con.commit()
        con.close()