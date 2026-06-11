class String():
    def __init__(self, s=""):
        self.s = s
    def reverse(self, s):
        self.s = s[::-1]
        return self.s
user = str(input("Enter a string value: "))
string = String(user)
print(f"The reverse of {user} is {string.reverse(user)}")