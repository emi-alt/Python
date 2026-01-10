print(f"Hello {input("what's your name? ")} , it's summertime! \nLet's decide what to do today! \nPlease only answer with yes or no to the following questions.")
if input("Do you want to go outside? ").lower() == "yes":
    print("Wear light, cotton clothes and sunglasses, eat ice cream to cool yourself down and take a white umbrella to protect yourself from the sun!")
    if input("Do you want to go to the beach? ").lower() == "yes":
        print("Don't forget your swimsuit, sunscreen and a towel!")
    else: 
        print("Then you can go to the park and drink something cold")
else:
    print("Then you can stay inside, drink a cold drink in front of a fan")