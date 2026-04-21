age = input("Please enter your age: ")
try:
    if int(age) % 2 == 0:
        print("Your age is an even number, ", age)
    elif int(age) % 2 != 0:
        print("Your age is an odd number, ", age)
    
    if int(age) < 10:
        print("You are too young to be using a device.")
    elif int(age) > 140:
        print("Enter your real age.")
except ValueError:
    print("Please enter an integer/whole number.")
except ZeroDivisionError:
    print("Division by zero is not possible.")
except:
    print("Something went wrong.")