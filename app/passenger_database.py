import sqlite3
import datetime


class PassengerDatabase:

    conn = sqlite3.connect('app/databases/passengers.db', check_same_thread=False)
    c = conn.cursor()

    def add_passenger(self, flight_id):
        query = "INSERT into " + flight_id + " (:passport_id,:first_name,:last_name,:dob)"
        with self.conn:
            self.c.execute(query, {
                'passport_id': self.passport_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'dob': self.dob
            })

    def book_flight_trip(self):
        pass

    def view_booking(self):
        pass


# pass1 = Passenger(31195344, 'Jacob', 'Sinclair', datetime.datetime(1994, 10, 21))
# pass2 = Passenger(83636482, 'Harry', 'Smith', datetime.datetime(2014, 4, 2))
# pass3 = Passenger(31195342, 'Karen', 'Fraser', datetime.datetime(2020, 12, 12))
#
# pass1.add_passenger()
# pass2.add_passenger()
# pass3.add_passenger()