"""
restaurants  таблица ресторанов
Поля
user_id  id пользователя
name название
address адрес


CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY  AUTOINCREMENT,
    name TEXT,
    address TEXT
);

"""

import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создаем таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT
);
''')



# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()


