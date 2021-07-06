from person import Person


class Passengers(Person):
    def __init__(self, passport_id, flight_id):
        super().__init__()
        self.passport_id = passport_id
        self.flight_id = flight_id

    def add_passenger(self):
        pass

    def book_flight_trip(self):
        pass

    def view_booking(self):
        pass

    def cancel(self):
        pass