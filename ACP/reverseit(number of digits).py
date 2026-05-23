number = input("Enter a number to count it's digits: ")
count = 0
for i in number:
    if int(i) > 0:
        count += 1
    elif int(i) == 0:
        print("No digits")
    else:
        print("Enter a valid number.")

print(f"The number of digits in the number {number} are {count}.")