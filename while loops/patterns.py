print("Tringle pattern")
n = int(input("Enter how many rows you want: "))
for i in range(n):
    for j in range(i+1):
        print("* ", end=" ")
    print()