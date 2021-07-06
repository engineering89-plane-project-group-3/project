import sqlite3

destinations_db = sqlite3.connect('databases/destinations.db')
destinations_db_cursor = destinations_db.cursor()


def database_initialise():
    destinations_db.execute("""CREATE TABLE IF NOT EXISTS destinations (
        destination text,
        distance real,
        time text,
    )""")

def add_destination(destination, distance, time):
    destinations_db_cursor.execute("INSERT INTO destinations VALUES (?, ?, ?)", (destination, distance, time))
    destinations_db.commit()

def remove_destination(destination):
    destinations_db_cursor.execute("DELETE FROM destinations WHERE ?", destination)
    destinations_db.commit()