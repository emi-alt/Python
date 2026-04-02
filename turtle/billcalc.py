def amount(bill, tip):
    total = bill*(1+0.01*tip)
    total = round(total, 2)
    print("Please pay $" + str(total))

amount(100,10)