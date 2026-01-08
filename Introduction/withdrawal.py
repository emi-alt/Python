amount = int(input("Enter the amount you want to withdraw: "))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print(f"You will recieve {note1} notes of 100 rupees, {note2} notes of 50 rupees and {note3} of 10 rupees.")
print("The total withdrawn amount is: ", amount)
