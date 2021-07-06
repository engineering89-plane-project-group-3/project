from aircraft import Aircraft
#from flight_trip import FlightTrip


class Helicopter(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def method(self):
        pass


class Aeroplane(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def method(self):
        pass
