import sqlite3 as sq

students = [(1, 'Маша', 2, 20), (2, 'Дима', 1, 21), (3, 'Саша', 1 , 22),
    (4, 'Кристина', 2, 23)]

marks = [(1, 'СИ', 3), (1, 'Физра', 4), (1, 'Матан', 3), (2, 'СИ', 4),
    (2, 'Физра', 5), (2, 'Матан', 4), (3, 'СИ', 5), (3, 'Физра', 5),
    (3, 'Матан', 5), (4, 'СИ', 4), (4, 'Физра', 4), (4, 'Матан', 4)]

with sq.connect("my_first_db.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER,
        old INTEGER
    )""")

    cur.executemany("INSERT OR IGNORE INTO students VALUES(?,?,?,?);", students)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS marks (
        
        id INTEGER,
        subject TEXT,
        mark INTEGER
    )""")

    cur.executemany("INSERT OR IGNORE INTO marks VALUES(?,?,?);", marks)
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS female (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER,
        old INTEGER
    )""")