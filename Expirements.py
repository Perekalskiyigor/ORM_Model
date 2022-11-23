import sqlite3

# con = sqlite3.connect('mydatabase.db')
# cursorObj = con.cursor()
# cursorObj.execute(f"SELECT COUNT(user.Column) FROM user")
# f = cursorObj.fetchall()
# print (f)
    
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


insert_value(["TEXT","Column","Digit"],["test","test","test"])


# print(f"IF NOT EXISTS(SELECT * FROM user.COLUMNS WHERE TABLE_NAME = 'user' "
#     f"AND COLUMN_NAME = 'fffff') "
#     f"BEGIN "
#     f"ALTER TABLE user ADD some_column TEXT "
#     f"END "
#     f"GO"
#     )


#     Проверка таблицы на наличие одной из записи проходит так:

# info = curs.execute('SELECT * FROM users WHERE id_telegram=?', (user_id, ))
# if info.fetchone() is None: 
#         #Делаем когда нету человека в бд
# else:
#         #Делаем когда есть человек в бд