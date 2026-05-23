n1 = input("Enter the start of the range of numbers: ")
n2 = input("Enter the end of the range of numbers: ")
ul = int(n1)
ll = int(n2)
nums = " "
squares = []
def square(ul, ll):
    n = []
    for i in range(ul, ll+1):
        n.append(i**2)
    return n
squares.extend(square(ul, ll))
print("Square of the range of numbers is ", squares)
even = []
odd = []
for i in squares:
    if i%2 == 0:
        print(f"The number {i} is an even number.")
        even.append(i)
    else:
        print(f"The number {i} is an odd number.")
        odd.append(i)
print(f"The list of even numbers is {even}.")
print(f"The list of odd numbers is {odd}.")