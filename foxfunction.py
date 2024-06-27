import sqlite3 as sql

fox_db = 'foxhole.db'
dracula_db = 'dracula.db'

def init_db(filename):
    conn = None
    try:
        conn = sql.connect(filename)
        print(sql.sqlite_version)
        print(f"{filename} created")
    except sql.error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def add_stockpile(ctx, location: str, code: str):
    conn = sql.connect(fox_db)
    cur = conn.cursor()
    cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
    conn.commit()
    conn.close()
    return location
