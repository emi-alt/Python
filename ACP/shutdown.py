print("Can't shutdown your computer? answer the following questions in y or n to shutdown your computer.")
def shutdown():
    q1 = input("is your work on the computer finished?")
    if q1 == "y":
        print("Shutting down...")
    elif q1 == "n":
        q2 = input("Is your computer heated up?")
        if q2 == "y":
            print("Sutting down...")
        elif q2 == "n": 
            q3 = input("Is your computer running slow?")
            if q3 == "y":
                print("Shutting down...")
            elif q3 == "n":
                q4 = input("Are you getting distracted by your computer?")
                if q4 == "y":
                    print("Shutting down...")
                elif q4 == "n":
                    q5 = input("Is there a problem with your computer that you cannot fix?")
                    if q5 == "y":
                     print("Shutting down...")
                    elif q1 == "n" or q2 == "n" or q3 == "n" or q4 == "n" or q5 == "n":
                        print("Abort shutown.")
                    else:
                        print("Sorry. Invalid input.")
                else:
                    print("Sorry. Invalid input.")
            else:
                print("Sorry. Invalid input.")
        else:
            print("Sorry. Invalid input.")
    else:
        print("Sorry. Invalid input.")
shutdown()
                    
                      