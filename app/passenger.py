from person import Person


class Passengers(Person):
    def __init__(self, passport_id):
        super().__init__()
        self.passport_id = passport_id

