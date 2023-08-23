# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним
# хранилищем информации, и чтоб был реализован основной функционал -
# просмотр, сохранение, импорт, поиск, удаление.
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях)
# или БД ГУИ можно сделать просто на EasyGUI или Tkinter

import sqlite3 as sq

with sq.connect("contacts.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    dr TEXT,
    mail TEXT
)""")

def add_contact():
    name = input("Имя: ")
    phone = input("Номер телефона: ")
    dr = input("Введите дату рождения: ")
    mail = input("Введите вашу почту: ")
    cur.execute(f"INSERT INTO contact (name, phone, dr, mail) VALUES('{name}','{phone}','{dr}','{mail}')")
    print("Контакт успешно сохранен.")
    con.commit()

def del_contact():
    names = input("Введите имя для удаления контакта: ")
    sql = f"DELETE FROM contact WHERE name = '{names}'"
    con.execute(sql)
    print("Контакт успешно удален.")
    con.commit()



def search_contact():
    search = input("Введите имя: ")
    cur.execute(f"select * from contact where name = '{search}'")
    for row in cur.fetchall():
        print(row)
        print(f"Контакт {search} найден.")
        break
    else:
        print("Контакт не найден, попробуйте еще раз ввести имя верно.")
        search_contact()


def show_data():  # показываем все записи таблицы users
    cur.execute("select * from contact")
    for row in cur.fetchall():
        print(row)
    print('Контакты успешно выгруженны!')

create_table()

while True:
    print("1. Добавить контакт.\n"
          "2. Удалить контакт.\n"
          "3. Показать все контакты.\n"
          "4. Найти контакт.")

    command = int(input("Введите номер команды: "))
    if command == 1:
        add_contact()
        break
    elif command == 2:
        del_contact()
        break
    elif command == 3:
        show_data()
        break
    elif command == 4:
        search_contact()
        break
    else:
        print("Вы ввели не существующий номер команды. ")

con.close()