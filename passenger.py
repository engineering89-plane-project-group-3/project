import sqlite3
from person import Person

conn = sqlite3.connect('databases/staff.db')
c = conn.cursor()

c.execute("""
CREATE TABLE passenger(
) """)

class Passengers(Person):
    def __init__(self, passport_id, flight_id,first_namegit a ,):
        super().__init__()
        self.passport_id = passport_id
        self.flight_id = flight_id

    def add_passenger(self):
        pass

    def book_flight_trip(self):
        pass

    def view_booking(self):
        pass

    def cancel

