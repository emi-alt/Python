import math
angle = input("Enter the angle in degrees: ")
def trignomtry():
    rad = math.radians(float(angle))
    pick = input(("pick a trignometric function: \n1. sin\n2. cos\n3. tan\n"))
    if pick == "1":
        print("The value of sin", angle, " in radians is ", math.sin(rad))
    elif pick == "2":
        print(f"The value of cos{angle} in radians is {math.cos(rad)}")
    elif pick == "3":
        print(f"The value of tan{angle} in radians is {math.tan(rad)}")
    else:
        print("Invalid input.")
trignomtry()