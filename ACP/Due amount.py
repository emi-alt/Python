bill = input("Enter the price/amount of item/items that you have bought: ")
pay = input("Enter the total money that you have: ")
if bill<pay:
    change = pay-bill
    print(f"The amount that the shopkeeper has to return back to you is {change}.")
elif bill>pay:
    change = bill-pay
    print(f"That's not enough to pay for that item. You need to pay {change} more to the shopkeeper.")
elif bill==pay:
    print("The amount paid and bill are equal. Therefore, the item is already fully paid for and there's no need for giving change amount.")
    pass