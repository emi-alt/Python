units = int(input("Enter number of units you have consumed: "))
if units <= 50:
    bill = units * 2.60
    suramt = 25
elif units <= 100:
    bill = 130 + (units - 50) * 3.25
    suramt = 35
elif units <= 200:
    bill = 130 + 162.50 + (units - 100) * 5.26
    suramt = 45
else:
    bill = 130 + 162.50 + 526 + (units - 200) * 8.45
    suramt = 75

total = bill + suramt
print("\nYour electricity bill is = %.2f" %total)