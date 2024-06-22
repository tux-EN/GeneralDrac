import sqlite3


def createSqliteDatabase(filename):
    connection = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.error as e:
        print(e)
    finally:
        if conn:
            conn.close
