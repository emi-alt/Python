Board = {"1": ' ', "2": ' ', "3": ' ', 
            "4": ' ', "5": ' ', "6": ' ', 
            "7": ' ', "8": ' ', "9": ' ', }

boardkey = []

for key in Board:
    boardkey.append(key)

def printboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn = "X"
    count = 0

    for i in range(10):
        printboard(Board)
        print(f"It's your turn, {turn}. Enter which place you wnt to go to?")

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1

        else:
            print("That place is already filled.\nMove to another place.")
            continue

        if count >= 5:
            if Board['1'] == Board['2'] == Board['3'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['4'] == Board['5'] == Board['6'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['7'] == Board['8'] == Board['9'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['1'] == Board['4'] == Board['7'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['2'] == Board['5'] == Board['8'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['3'] == Board['6'] == Board['9'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['1'] == Board['5'] == Board['9'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
            elif Board['3'] == Board['5'] == Board['7'] != " ":
                printboard(Board)
                print("\nGame Over.\n")
                print(f"~~~~~ {turn} ~~~~~")
                break
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!")
        if turn == "X":
            turn = 'O'
        else:
            turn = "X"
    restart = input("Do you want to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in boardkey:
            Board[key] = " "

        game()

if __name__ == "__main__":
    game()