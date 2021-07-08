import sqlite3


class PassengerDatabase:

    conn = sqlite3.connect('app/databases/passengers.db', check_same_thread=False)
    c = conn.cursor()

    def add_passenger(self, flight_id, passport_id, first_name, last_name, dob):
        self.c.execute("""CREATE TABLE IF NOT EXISTS {}  ( 
            passport_id text, 
            first_name text, 
            last_name text, 
            dob text 
        )""".format(flight_id))
        self.c.execute('INSERT INTO ' + flight_id + ' VALUES (?, ?, ?, ?)',
                       (passport_id, first_name, last_name, dob))
        self.conn.commit()

    def book_flight_trip(self):
        pass

    def view_booking(self):
        pass
