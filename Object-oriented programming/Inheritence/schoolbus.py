class Vehicle:
    def __init__(self, name, maxs, mileage):
        self.name = name
        self.maxs = maxs
        self.mileage = mileage

class Bus(Vehicle):
    pass

schoolbus = Bus("school volvo", 120, 12)
print(f"The name of the school bus is {schoolbus.name}. It's max speed is {schoolbus.maxs}. It's mileage is {schoolbus.mileage}.")