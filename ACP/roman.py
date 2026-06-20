class Roman(object):
    def __init__(self, num):
        self.num = num
        global mapping
        mapping = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
            100: "C"
        }
    def calc(self, num):
        
integer = int(input("Enter a number between 1 to 100 to convert it into roman number: "))
roman = Roman(integer)
print(f"The roman number is {roman.calc(integer)}.")