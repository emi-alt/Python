import random
playing = True
num = random.randint(0, 9)
print("I will generate a number from 0 to 9, and you have to guess the number.")
print("The game ends when you win!")
while playing:
  guess = int(input("Pick a number from 0 to 9 \n"))
  if num == guess:
    print("You won!")
    print("The number was ", num)
    break
  else:
    print("Oops! wrong guess! try again.")