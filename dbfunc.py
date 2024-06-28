import sqlite3 as sql

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