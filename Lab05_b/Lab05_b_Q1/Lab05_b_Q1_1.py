class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

my_vehicle = Vehicle(240, 18)

print(my_vehicle.max_speed, my_vehicle.mileage)