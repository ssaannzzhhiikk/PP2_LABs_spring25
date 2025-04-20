import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="Albatros2143"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица phonebook создана.")

def init_procedures():
    conn = connect()
    cur = conn.cursor()

    procedures = [

        # поиск по паттерну
        """
        CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
        RETURNS SETOF phonebook AS $$
        BEGIN
            RETURN QUERY
            SELECT p.*
            FROM phonebook p
            WHERE p.name ILIKE '%' || pattern || '%'
               OR p.phone LIKE '%' || pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
        """,

        # вставка или обновление юзера
        """
        CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, userphone TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = username) THEN
                UPDATE phonebook SET phone = userphone WHERE name = username;
            ELSE
                INSERT INTO phonebook(name, phone) VALUES (username, userphone);
            END IF;
        END;
        $$;
        """,

        # функция для batch вставки с возвратом некорректных данных
        """
        CREATE OR REPLACE FUNCTION insert_users_batch(usernames TEXT[], userphones TEXT[])
        RETURNS TEXT[] AS $$
        DECLARE
            i INT := 1;
            invalid_list TEXT[] := '{}';
        BEGIN
            WHILE i <= array_length(usernames, 1) LOOP
                IF userphones[i] ~ '^\\+?\\d{10,15}$' THEN
                    CALL insert_or_update_user(usernames[i], userphones[i]);
                ELSE
                    invalid_list := array_append(invalid_list, usernames[i] || ':' || userphones[i]);
                END IF;
                i := i + 1;
            END LOOP;
            RETURN invalid_list;
        END;
        $$ LANGUAGE plpgsql;
        """,

        # пагинация
        """
        CREATE OR REPLACE FUNCTION get_paginated_users(lim INT, offs INT)
        RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            ORDER BY id
            LIMIT lim OFFSET offs;
        END;
        $$ LANGUAGE plpgsql;
        """,

        #удаление по имени или телефону
        """
        CREATE OR REPLACE PROCEDURE delete_user_proc(username TEXT DEFAULT NULL, userphone TEXT DEFAULT NULL)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF username IS NOT NULL THEN
                DELETE FROM phonebook WHERE name = username;
            ELSIF userphone IS NOT NULL THEN
                DELETE FROM phonebook WHERE phone = userphone;
            END IF;
        END;
        $$;
        """
    ]

    for p in procedures:
        cur.execute(p)

    conn.commit()
    cur.close()
    conn.close()
    print("Функции и процедуры созданы.")

# Вызовы SQL

def insert_or_update(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv_batch(path):
    conn = connect()
    cur = conn.cursor()
    names, phones = [], []

    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue
            names.append(row[0].strip())
            phones.append(row[1].strip())

    cur.execute("SELECT * FROM insert_users_batch(%s, %s)", (names, phones))
    invalid = cur.fetchall()

    if invalid and any(i[0] for i in invalid):
        print("Некорректные данные:")
        for entry in invalid:
            print(entry[0])
    else:
        print("Все записи добавлены корректно.")
    cur.close()
    conn.close()

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_user(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user_proc(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# Меню
def menu():
    create_table()
    init_procedures()

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить пользователя вручную")
        print("2 - Добавить пользователей из CSV")
        print("3 - Найти пользователя по шаблону")
        print("4 - Удалить пользователя")
        print("5 - Показать всех с пагинацией")
        print("0 - Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update(name, phone)

        elif choice == "2":
            path = input("Путь к CSV-файлу: ")
            insert_from_csv_batch(path)

        elif choice == "3":
            pattern = input("Введите шаблон поиска (имя или телефон): ")
            search_by_pattern(pattern)

        elif choice == "4":
            by = input("Удалить по (n) имени или (p) телефону? ")
            if by == "n":
                name = input("Имя: ")
                delete_user(name=name)
            elif by == "p":
                phone = input("Телефон: ")
                delete_user(phone=phone)

        elif choice == "5":
            limit = int(input("Сколько записей: "))
            offset = int(input("С какого номера начать: "))
            get_paginated(limit, offset)

        elif choice == "0":
            print("До встречи!")
            break

        else:
            print("Неверный выбор. Повторите.")

if __name__ == "__main__":
    menu()
