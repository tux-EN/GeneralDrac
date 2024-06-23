import sqlite3

def initstockpileDB(filename):
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