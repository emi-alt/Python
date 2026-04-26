num = input("Please enter a list of single digit numbers: ")
odd = []
even = []
even = [x for x in num if int(x) % 2 == 0]
print("The even numbers are ",even)
odd = [x for x in num if int(x) % 2 != 0]
print("The odd numbers are ",odd)

fruits = ['apple', 'banana', 'pineapple', 'kiwi', 'orange', 'guava']
frt = list(map(str.capitalize,fruits))
print(frt)