import datetime
import sqlite3
from flight_trip import FlightTrip
from person import Person
from datetime import date

conn = sqlite3.connect('databases/passengers.db')
c = conn.cursor()


class Passenger(Person):

    def create_passenger_list(flight_id):
        query = f"""
        CREATE TABLE IF NOT EXISTS {flight_id}(
        passport_id integer, 
        first_name text,
        last_name text,
        dob text)"""
        with conn:
            return c.execute(query)

    def add_passenger_to_list(flight_id, passport_id, first_name, last_name, dob):
        query = f"INSERT into {flight_id} VALUES (:passport_id,:first_name,:last_name,:dob)"
        with conn:
            c.execute(query, {
                'passport_id': passport_id,
                'first_name': first_name,
                'last_name': last_name,
                'dob': dob
            })

    def view_passenger_list(flight_id):
        query = f"SELECT * FROM {flight_id}"
        with conn:
            c.execute(query)
            return c.fetchall()

    def remove_passenger(flight_id, passport_id):
        query = f"DELETE FROM {flight_id} WHERE passport_id = :passport_id"
        with conn:
            return c.execute(query, {'passport_id': passport_id})

    def view_passenger_flight_trip(flight_id):
        query = """
        SELECT * from flight_trip
        WHERE :flight_id = flight_trip.flight_id"""
        with conn:
            c.execute(query, {'flight_id': flight_id})
            return c.fetchone()
