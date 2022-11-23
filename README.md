# ORM_Model
Для корректной работы необходима бибилотека sqlite3
Модель упрощенная и поддерживает, только некоторые функции. Ниже описаны методы и прнцип работы с ними.
Для подключения в проект необходимо импортировать модуль.

Создание полей таблицы

Текстовое поле
Model = OrmText()
Model.create_value('Column')

Числовое поле
Model = OrmInteger()
Model.create_value('Digit')


Изменение записей и таблицы
delete_value - Удаляет таблицу. В метод необходимо передать имя таблицы
Model = OrmModel()
Model.delete_value('user')

insert_value - Вставляет указанное значение в бд
Формат ввотда. Методу передается список с именами колонок 
в которые производится вставка и передается список значений непосредвтенно, 
в том же порядке следования
insert_value(["TEXT","Column","Digit"],["test","test","test"])

update_value - Метод обновляет значение в бд по id
update_value (column_name,id,value):
column_name - имя колонки где произвести изменение
id - id записи
value - значение которое нужно вставить
insert_value(["TEXT","Column","Digit"],["test","test","test"])

filter_value - Метод поиска по значению
filter_value (columns_for_show,column_for_search, value)
columns_for_show - какие колонки показать на выходе
column_for_search - в какой колонке искать
value - какое значение искать
filter_value('TEXT, Column, Digit', 'Column', '2')