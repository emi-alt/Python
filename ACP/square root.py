num = float(input("Enter a number to find it's square root: "))
n = 1
for i in range(1, n+1):
    if n*n == num:
        square_root = num/n
        print("The square root of ", num, " is ", n)
        break
   
else: 
    print("The number is not a perfect square.")