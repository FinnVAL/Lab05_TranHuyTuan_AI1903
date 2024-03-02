class Vehicle:

    def __init__(self, name,mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity *100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        final_amount = total_fare + maintenance_charge
        return final_amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())