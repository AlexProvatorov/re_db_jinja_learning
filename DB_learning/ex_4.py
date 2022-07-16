import sqlite3 as sq

games = [(1, 300, 3000), (2, 400, 3500), (1, 500, 3800), (3, 200, 2000),
    (1, 500, 3600), (2, 400, 3000), (4, 200, 3000), (5, 800, 5000),
    (6, 500, 3000), (6, 300, 3000), (7, 400, 3600)]

with sq.connect("my_first_db.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS games(
        user_id INTEGER,
        score INTEGER,
        time INTEGER    
    )""")

    cur.executemany("INSERT INTO games VALUES(?,?,?);", games)
    con.commit()