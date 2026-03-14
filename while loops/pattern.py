row = int(input("Enter the number of rows: "))
if row%2 == 0:
    halfrow = int(row/2)
else:
    halfrow = int(row/2)+1
space = halfrow-1
#uppertriangle
for i in range(1, halfrow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()