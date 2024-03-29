import sqlite3 as sq

with sq.connect("my_first_db.db") as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_in INTEGER, buy INTEGER);
    """)

    cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    last_row_id = cur.lastrowid
    by_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Фёдор', ?, ?)", (last_row_id, by_car_id))