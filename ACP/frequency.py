dict = {1:"hello", 2:"tiara", 3:"nimo", 4:"nimo", 5:"tiara", 6:"tiara"}
print(dict)
freq = 0
word = input("Please enter the word of which you want to check the frequency of: ")
for f, w in dict.items():
    if w == word:
        freq += 1
print(f"The value {word} comes {freq} times in this dictionary.")