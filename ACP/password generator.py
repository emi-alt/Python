import random
import string
all_letters = list(string.ascii_letters)
print("Welcome to random password creater.\nWhere we create a 8 characters long password.")
passw = " "
i = " "
j = 0
""" for i in range(4):
    i = random.choice(all_letters)
    passw.append[i]
for j in range(4):
    j = random.randint(0, 100)
    passw.append[j]
print(passw) """
p = " "
y = 0
for i in range(8):
    p = random.choice(all_letters)
    i += 1
    if i > 4:
        y = random.randint(0, 100)
print(p,y)