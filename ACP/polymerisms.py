class BMW:
    def fuel_type(self):
        print("A BMW works on petrol.")
    def max_speed(self):
        print("BMW's max speed is 307km/h.")
class Ferrari:
    def fuel_type(self):
        print("A Ferrari works on petrol.")
    def max_speed(self):
        print("Ferrari's max speed is 352 km/h.")

obj_BMW = BMW()
obj_Ferrari = Ferrari()
for vehicle in obj_BMW, obj_Ferrari:
    print(vehicle.fuel_type( ))
    print(vehicle.max_speed( ))