from datetime import date
print("Hello! Welcome to Birthday Collector.")
name = input("Please enter your name: \n")
year = input("Please enter your birth year(in the form of YYYY): \n")
birthdate = input("Please enter your birth date(in the form of DD-MM): \n")
age = date.today().year - int(year)
print(f"Hello! {name}\n I will wish you a happy birthday on {birthdate}\n when you'll be {age} years old.")
