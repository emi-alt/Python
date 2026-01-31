#for loop
n = int(input("Enter the number whose sum you want: "))
sum = 0

for i in range(1,n+1):
    sum = sum+i
print("The sum is:", sum)

string = input("Please enter a word: ")
string2 = (' ')
for i in string:
    string2 = i + string2
print("The reverse of ", string, " is ", string2)

#reverse 
n = int(input("Enter a number to reverse count: "))
for i in range(n, 0, -1):
    print(i)
