def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("The factorial of 0 is ", factorial(0))
print("The factorial of 1 is ", factorial(1))
print("The factorial of 6 is ", factorial(6))
print("The factorial of 10 is ", factorial(10))