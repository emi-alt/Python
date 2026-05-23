number = int(input("Enter a number to convert into binary number: "))
num = number
t = " "
string = " "
while num > 0:
    t = str(num%2)
    string += str(t)
    num = num//2
reverse_t = string[::-1]
print(f"The number {number} in binary code is {reverse_t}.")