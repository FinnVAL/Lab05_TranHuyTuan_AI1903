class Vehicle:

    def __init__(self, name,mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

bus_class = type(School_bus)
print(bus_class)