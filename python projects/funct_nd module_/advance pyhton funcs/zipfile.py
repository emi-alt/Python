n1 = {4,5,6}
n2 = {"u","y","r"}
n3 = list(zip(n1,n2))
print(n3,"\n")

l1 = [10,20,30,40]
l2 = [100,200,300,400]
for x, y in zip(l1[::-1],l2):
    print(x,y)

stocks = ["reliance", "infosys", "tcs"]
price = [2175, 1127, 2750]
dict = {stocks: price for stocks, price in zip(stocks,price)}
print("\n{}".format(dict))