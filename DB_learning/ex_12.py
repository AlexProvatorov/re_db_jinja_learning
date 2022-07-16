import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    with open("sql_dump.sql", "w") as file_object:
        for sql in con.iterdump():
            file_object.write(sql)

    with open("sql_dump.sql", "r") as file_object:
        sql = file_object.read()
        cur.executescript(sql)