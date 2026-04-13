l = [7,3,7,6,9,2,1,4,9,5]
print("Original list: ", l)

count = 0
for i in l:
    count += i

avg = count / len(l)
print("The average of the list is ", avg)

l.sort()
print("In ascending order: ", l)

print("Smallest number in the list is ", l[0])
print("Largest number in the list is ", l[-1])