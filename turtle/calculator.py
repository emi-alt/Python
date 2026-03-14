def add(P,Q):
    return P + Q 
def subtract(P,Q):
    return P - Q 
def multiply(P,Q):
    return P*Q 
def divide(P,Q):
    return P/Q

print("Welcome to the calculator")
print("Please choose an operation:")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
opr = input("Enter your choice (a/b/c/d): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if opr == 'a':
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif opr == 'b':
    print(f"{num1} - {num2} = {subtract(num1,num2)}")
elif opr == 'c':
    print(f"{num1} * {num2} = {multiply(num1,num2)}")
elif opr == 'd':
    print(f"{num1} / {num2} = {divide(num1,num2)}")

else: 
    print("Invalid choice.")