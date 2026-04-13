actual_cost = float(input("Please enter the actual cost of product(s): "))
sale_amount = float(input("Please enter the slae amount:"))

if (sale_amount > actual_cost):
  amount = sale_amount - actual_cost
  print("Total profit = {0}".format(round(amount, 2)))
else:
  print("No profit!")