import sqlite3 as sq

cars = [
    ('Ford', 16896),
    ('Lada', 11296),
    ('UAZ', 12588)
]

with sq.connect("my_first_db.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

    cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})
