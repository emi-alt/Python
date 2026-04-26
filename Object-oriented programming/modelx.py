class Vehicle():
    def __init__(self, max_v, mileage):
        self.max_v = max_v
        self.mileage = mileage

modelX = Vehicle(220, 16)
modelY = Vehicle(250, 19)
print("The max speed of model X is", modelX.max_v)
print("The mileage of model X is", modelX.mileage)
print("The max speed of model Y is", modelY.max_v)
print("The mileage of model Y is", modelY.mileage)