class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if (self.a < other.a):
            return f"{self.a} is lesser than {other.a}."
        else:
            return f"{self.a} is greater than {other.a}."
        
    def __eq__(self, other):
        if (self.a == other.a):
            return f"{self.a} is equal to {other.a}"
        else:
            return f"{self.a} and {other.a} are not equal."
    
ob1 = A(2)
ob2 = A(3)

print("Passing values: ", ob1.a, ob2.a)
print(ob2 < ob1)

ob3 = A(5)
ob4 = A(5)
print("Passign values ", ob3.a, ob4.a)
print(ob3 == ob4)