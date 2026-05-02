import random
import string
all_letters = list(string.ascii_letters)
print("Welcome to random password creater.\nWhere we create a 8 characters long password.")
passw = " "
for i in range(4):
    passw += random.choice(all_letters)
for j in range(4):
    passw += str(random.randint(0, 10))
print(passw)

""" import random

import string

all_letters = list(string.ascii_letters)

print("Welcome to random password creator.\nWhere we create an 8 character long password.")

password = ""

# Add 4 random letters

for _ in range(4):

  password += random.choice(all_letters)

# Add 4 random digits

for _ in range(4):

  password += str(random.randint(0, 9))

print("Your password is:", password) """