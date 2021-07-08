import sqlite3


class FlightTrip:
    flight_trip_db = sqlite3.connect('app/databases/flight_trip.db', check_same_thread=False)
    flight_trip_db_cursor = flight_trip_db.cursor()

    destinations_db = sqlite3.connect('app/databases/destinations.db', check_same_thread=False)
    destinations_db_cursor = destinations_db.cursor()

    def database_initialise(self):
        self.flight_trip_db_cursor.execute("""CREATE TABLE IF NOT EXISTS flight_trip (
            flight_id text,
            aircraft_id text,
            capacity integer,
            destination text,
            departure_time text,
            arrival_time text,
            terminal_id text,
            price real
        )""")

    def create_flight_trip(self, flight_id, aircraft_id, capacity, destination, departure_time, arrival_time):
        self.destinations_db_cursor.execute("SELECT distance FROM destinations WHERE destination = (?)", (destination,))
        distance = self.destinations_db_cursor.fetchone()[0]
        price = 0.10 * distance

        self.flight_trip_db_cursor.execute("INSERT INTO flight_trip VALUES (?, ?, ?, ?, ?, ?, ?)",
                                           (flight_id, aircraft_id, capacity, destination, departure_time, arrival_time, price))
        self.flight_trip_db.commit()
#def available_seats()
    def change_flight_trip(self):
        pass

    def available_flights(self):
        self.flight_trip_db_cursor.execute("SELECT flight_id, destination from flight_trip")
        return self.flight_trip_db_cursor.fetchall()

    def view_flight_trip(self, flight_id):
        self.flight_trip_db_cursor.execute("SELECT * FROM flight_trip WHERE flight_id = (?)", (flight_id,))
        return self.flight_trip_db_cursor.fetchall()

d = FlightTrip()
d.database_initialise()