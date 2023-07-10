class CarFactory:
    def __init__(self):
        self.models = {}

    def register_model(self, model, engine, battery, tires):
        self.models[model] = {
            'engine': engine,
            'battery': battery,
            'tires': tires
        }

    def create_car(self, model, tire_wear):
        if model in self.models:
            engine = self.models[model]['engine']()
            battery = self.models[model]['battery']()
            tires = self.models[model]['tires'](tire_wear)

            return Car(model, engine, battery, tires)
        else:
            raise ValueError("Invalid car model")

class CarriganTires:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tire_wear)

class OctoprimeTires:
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        return sum(self.tire_wear) >= 3
