class Vehicle:
    global pay
    def __init__(self, capacity):
        self.capacity = capacity
        pass
    def payment(self, pay, capacity):
        self.pay = self.capacity * 100
        return self.pay
class Bus(Vehicle):
    global fare
    def bus_fare(self, pay, capacity):
        self.fare = self.pay + self.pay*1/10
        return self.fare

purple_bus = Bus(50)
print(f"Any vehicle's fare is {purple_bus.payment(20, 20)}")
print(f"The bus fare is {purple_bus.bus_fare(20, 20)}")