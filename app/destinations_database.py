import sqlite3


class DestinationsDatabase:
    destinations_db = sqlite3.connect('app/databases/destinations.db', check_same_thread=False)
    destinations_db_cursor = destinations_db.cursor()

    def database_initialise(self):
        self.destinations_db.execute("""CREATE TABLE IF NOT EXISTS destinations (
            destination text,
            distance real,
            time text,
        )""")

    def add_destination(self, destination, distance, time):
        self.destinations_db_cursor.execute("INSERT INTO destinations VALUES (?, ?, ?)", (destination, distance, time))
        self.destinations_db.commit()

    def remove_destination(self, destination):
        self.destinations_db_cursor.execute("DELETE FROM destinations WHERE ?", destination)
        self.destinations_db.commit()
