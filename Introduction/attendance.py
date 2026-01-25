med = input("Do you have a medical condition? (Y/N): ").strip().upper()

attendance = int(input("What is your attendance? (1-100): ").strip())
if med == 'Y':
    print("You are allowed.")
else:
    if attendance >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")