import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER)
    """)

    #cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    cur.execute("SELECT model, price FROM cars")

    for result in cur:
        print(result['model'], result['price'])