n = int(input("Enter the number of rows: "))
i = 0
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
for p in range(n-1, 0,-1):
    for t in range(p):
        print("*", end=" ")
    print()