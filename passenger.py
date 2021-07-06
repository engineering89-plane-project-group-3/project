import sqlite3
import datetime
from person import Person

conn = sqlite3.connect('databases/passengers.db')
c = conn.cursor()

c.execute("""
CREATE TABLE passengers(
passport_id integer,
first_name text,
last_name text,
dob text)""")


class Passengers(Person):
    def __init__(self, passport_id, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.passport_id = passport_id

    def add_passenger(self):
        query = "INSERT into passengers VALUES (:passport_id,:first_name,:last_name,:dob)"
        with conn:
            c.execute(query, {
                'passport_id': self.passport_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'dob': self.dob
            })

    def book_flight_trip(self):
        pass

    def view_booking(self):
        pass


pass1 = Passengers(31195344, 'Jacob', 'Sinclair', datetime.datetime(1994, 10, 21))
pass2 = Passengers(83636482, 'Harry', 'Smith', datetime.datetime(2014, 4, 2))
pass3 = Passengers(31195344, 'Karen', 'Fraser', datetime.datetime(2020, 12, 12))

pass1.add_passenger()
pass2.add_passenger()
pass3.add_passenger()
