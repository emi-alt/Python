print("To enter my class you must be between 10 and 20years old.")
age = int(input("Enter your age: "))
if age <= 10:
    print("you are too young to enter my enter my class.")
else:
    if age <= 20:
        print("You are old enough to enter my class.")
        print("Welcome to my class.")
    else:
        print("You are too old to enter my class.")
