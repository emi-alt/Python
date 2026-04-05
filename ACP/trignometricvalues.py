import math
def trignomtry():
    angle = input("Enter the angle in degrees: ")
    rad = math.radians(float(angle))
    pick = input(("pick a trignometric function: \n1. sin\n2. cos\n3. tan"))
    if pick == "1":
        print("The value of sin ", angle, " in radians is ", math.sin(rad))
    elif pick == "2":
        print("")