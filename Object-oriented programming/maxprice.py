class Price:
    def __init__(self):
        self.__maxprice = 500
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Price()
c.sell()

c.__maxprice = 1000
c.sell()
 
c.setMaxPrice(1000)
c.sell()