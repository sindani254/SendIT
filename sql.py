import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE parcels(name TEXT, qty INT, sender TEXT) ")
    c.execute('INSERT INTO parcels VALUES("smartphone", 2, "manu")')
