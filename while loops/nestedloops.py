w = str(input("Enter a string: "))
char = str(input("Enter a character: "))
i = 0
count = 0
while (i< len(w)):
    if w[i] == char:
        count = count + 1
    i = i + 1
print("The number of times ", char, " appears in", w, "is ", count)