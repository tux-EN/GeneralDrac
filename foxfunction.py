import sqlite3

dbName = 'foxhole.db'

def initDB(filename):
    conn = None
    stocktable="""CREATE TABLE STOCKPILES (
        Location VARCHAR(255) NOT NULL,
        Code INT(6)
        );"""
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
        fcursor=conn.cursor()
        fcursor.execute(stocktable)
        print("DBand Tables created")
    except sqlite3.error as e:
        print(e)
    finally:
        if conn:
            conn.close


def addStockpile(ctx, location: str, code: str):
    conn = sqlite3.connect(dbName)
    cur = conn.cursor()
    cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
    conn.commit()
    conn.close
    return location