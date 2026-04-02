print("Welcome! This application will convert decimal number to binary.")
'''This is a recursive function to convert a decimal number to binary.'''
n = int(input("Enter a decimal number: "))
def binary(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while n>1 and n%2 != 0:
            return binary(n%2)
    
print("The binary number of ", n, " is ", binary(n))