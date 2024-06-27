import sqlite3 as sql

foxDb = 'foxhole.db'


def init_db(filename):
    conn = None
    try:
        conn = sql.connect(filename)
        print(sql.sqlite_version)
        print(f"{filename} DB and Tables created")
    except sql.error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def add_stockpile(ctx, location: str, code: str):
    conn = sql.connect(foxDb)
    cur = conn.cursor()
    cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
    conn.commit()
    conn.close()
    return location
