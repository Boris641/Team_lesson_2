"""
users таблица категорий блюд
Поля
category_id   id категории
name имя категории
descr описание категории

CREATE TABLE categorys (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    descr TEXT NOT NULL
)


"""

import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../mydatabase.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE categorys (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    descr TEXT NOT NULL
)
''')


# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()