import sqlite3
import datetime

flight_trip_db = sqlite3.connect('databases/flight_trip.db')
flight_trip_db_cursor = flight_trip_db.cursor()

destinations_db = sqlite3.connect('databases/destinations.db')
destinations_db_cursor = destinations_db.cursor()

def database_initialise():
    flight_trip_db_cursor.execute("""CREATE TABLE IF NOT EXISTS flight_trip (
        flight_id text,
        aircraft_id text,
        capacity integer,
        destination text,
        departure_time text,
        arrival_time text,
        terminal_id text,
        price real
    )""")

def create_flight_trip(flight_id, aircraft_id, capacity, destination, departure_time, arrival_time, terminal_id):
    destinations_db_cursor.execute("SELECT distance FROM destinations WHERE destination = (?)", (destination,))
    distance = destinations_db_cursor.fetchone()[0]
    price = 0.10 * distance

    flight_trip_db_cursor.execute("INSERT INTO flight_trip VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
    flight_id, aircraft_id, capacity, destination, departure_time, arrival_time, terminal_id, price))
    flight_trip_db.commit()

def change_flight_trip():
    pass

def available_flights():
    flight_trip_db_cursor.execute("SELECT flight_id, destination from flight_trip")
    return flight_trip_db_cursor.fetchall()

def view_flight_trip(flight_id):
    flight_trip_db_cursor.execute("SELECT * FROM flight_trip WHERE flight_id = (?)", (flight_id,))
    return flight_trip_db_cursor.fetchall()

create_flight_trip("BA_003", "3", "200", "Athens", "14:00", "17:45", "B")