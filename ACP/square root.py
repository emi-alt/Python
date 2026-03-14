num = float(input("Enter a number to find it's square root: "))
n = 1
for i in range(1, n+1):
    if i*i == num:
        square_root = num/i
        print("The square root of ", num, " is ", i)
        break
   
else: 
    print("The number is not a perfect square.")