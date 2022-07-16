import sqlite3 as sq

with sq.connect("my_first_db.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    result = cur.fetchone()
    result_2 = cur.fetchmany(4)

    print(result)
    print(result_2)