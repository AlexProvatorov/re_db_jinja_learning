import sqlite3 as sq
from sqlite3.dbapi2 import Binary

def readAva(n):
    # Читает аватарки.
    try:
        with open(f"avas/{n}.png", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False

def writeAva(name, data):
    try:
        with open(name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True

with sq.connect("users.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        ava BLOB,
        score INTEGER)
    """)

    #img = readAva(1)
    #if img:
    #    binary = sq.Binary(img)
    #    cur.execute("INSERT INTO users VALUES ('София', ?, 1000)", (binary,))

    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']

    writeAva("out.png", img)