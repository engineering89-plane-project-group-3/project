import sqlite3


class FlightTrip:

    passenger_list = []

    def __init__(self, flight_id, aircraft_id, destination, departure_time, arrival_time,terminal_id,price):
        self.flight_id = flight_id
        self.aircraft_id = aircraft_id
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price

    def create_flight_trip(self):
        pass

    def add_passenger_to_list(self):
        pass

    def remove_passenger_from_list(self):
        pass

    def view_passenger_list(self):
        pass

    def change_flight_trip(self):
        pass

    def view_flight_trip(self):
        pass

    def calculate_price(self, age, destination):
        pass

