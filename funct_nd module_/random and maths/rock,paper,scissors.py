import random
while True:
  user = input("Choose an option(rock, paper, scissors)")
  actions = ["rock", "paper", "scissors"]
  computer = random.choice(actions)
  print(f"You chose {user} and the computer chose {computer}.")

  if user == computer:
    print("You both chose ", user, ". It's a tie!")
  elif user == "rock":
    if computer == "scissors":
      print("Rock smashes scissors. You win!")
    else:
      print("Paper covers rock. You lose.")
  elif user == "paper":
    if computer == "rock":
      print("Paper covers rock. You win!")
    else:
      print("Scissors cuts paper. You lose.")
  elif user == "scissors":
    if computer == "paper":
      print("Scissors cuts paper. You win!")
    else:
      print("Rock smashes scissors. You lose.")

  play_again = input("Play again? (y/n): ")
  if play_again != "y":
   break