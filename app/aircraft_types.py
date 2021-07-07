from aircraft import Aircraft

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
