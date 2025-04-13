import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="snake",
        user="postgres",
        password="Albatros2143"
    )


def search_user(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM snake")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

search_user()