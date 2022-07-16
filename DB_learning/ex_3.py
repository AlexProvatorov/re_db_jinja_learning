import sqlite3 as sq

with sq.connect("my_second_db.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS games""")

    cur.execute("""CREATE TABLE IF NOT EXISTS games (

        user_id INTEGER,
        score INTEGER,
        time INTEGER
    )""")