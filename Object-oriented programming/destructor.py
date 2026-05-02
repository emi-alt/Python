class IOString():
    def __init__(self):
        self.str = ""
    def get_string(self):
        self.str = input("Enter a string: ")
    def print_string(self):
        print("The result is", self.str.upper())

str1 = IOString()
str1.get_string()
str1.print_string()