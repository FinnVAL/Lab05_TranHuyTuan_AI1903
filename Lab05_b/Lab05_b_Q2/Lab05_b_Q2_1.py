class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

my_bus = Bus("School Volvo", 180, 12)
print(f"Vehicle Name: {my_bus.name} Speed: {my_bus.max_speed} Mileage: {my_bus.mileage}")