num1 = [1, 3, 5]
num2 = [2, 4, 6]
add = map(lambda x, y: x + y, num1, num2)
print(f"The addition of these two lists is: {list(add)}")

num = [4, 5, 6, 7, 8]
def sq(r):
    return r*r
l = map(sq, num)
print("The list of squares of a list is ", list(l))