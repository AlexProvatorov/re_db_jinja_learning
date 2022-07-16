import sqlite3 as sq
from sqlite3.dbapi2 import connect

con = None

try:
    con = connect("my_first_db.db")
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL, 'Audi', 24868);
        INSERT INTO cars VALUES(NULL, 'BMW', 28967);
        INSERT INTO cars VALUES(NULL, 'Mazda', 26957)
    """)

    con.commit()

except sq.Error as e:
    if con: con.rollback()
    print("Ошибка выполнения запроса")

finally:
    if con: con.close()

    #cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    #    UPDATE cars SET price = price + 1000
    #""")