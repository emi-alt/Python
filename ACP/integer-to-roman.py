class Roman(object):
    def __init__(self, num):
        self.num = num
        global mapping
        self.mapping = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
            100: "C"
        }
    def calc(self, num):
        global roman
        global p
        if 10 < self.num < 20:
            self.p = self.num - 10
            self.roman = self.mapping[10] + self.mapping[self.p]
            return self.roman
        elif 20 < self.num < 30:
            self.p = self.num - 20
            self.roman = self.mapping[20] + self.mapping[self.p]
            return self.roman
        elif 30 < self.num < 40:
            self.p = self.num - 30
            self.roman = self.mapping[30] + self.mapping[self.p]
            return self.roman
        elif 40 < self.num < 50:
            self.p = self.num - 40
            self.roman = self.mapping[40] + self.mapping[self.p]
            return self.roman
        elif 50 < self.num < 60:
            self.p = self.num - 50
            self.roman = self.mapping[50] + self.mapping[self.p]
            return self.roman
        elif 60 < self.num < 70:
            self.p = self.num - 60
            self.roman = self.mapping[60] + self.mapping[self.p]
            return self.roman
        elif 70 < self.num < 80:
            self.p = self.num - 70
            self.roman = self.mapping[70] + self.mapping[self.p]
            return self.roman
        elif 80 < self.num < 90:
            self.p = self.num - 80
            self.roman = self.mapping[80] + self.mapping[self.p]
            return self.roman
        elif 90 < self.num < 100:
            self.p = self.num - 90
            self.roman = self.mapping[90] + self.mapping[self.p]
            return self.roman
        else:
            self.p = self.mapping[100]
integer = int(input("Enter a number between 1 to 100 to convert it into roman number: "))
roman = Roman(integer)
print(f"The roman number is {roman.calc(integer)}.")