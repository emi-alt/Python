class Animal:
     def __init__(self, breed, colour):
         self.breed = breed
         self.colour = colour
G_R_obj = Animal("Golden Retriever", "Golden")
Poodle_obj = Animal("Poodle", "White")
print(f"First animal is a {G_R_obj.breed}, It's colour is {G_R_obj.colour}.")
print(f"Second animal is a {Poodle_obj.breed}, It's colour is {Poodle_obj.colour}.")