print("Please only enter one syllabule.")
alphabet = str(input("Enter a character: "))
alpha = ['q', 'w','e', 'r','t', 'y','u', 'i','o', 'p','a', 's','d', 'f','g', 'h','j', 'k','l', 'z','x', 'c', 'v','b', 'n', 'm'
         ,'Q', 'W','E', 'R','T', 'Y','U', 'I','O', 'P','A', 'S','D', 'F','G', 'H','J', 'K','L', 'Z','X', 'C', 'V','B', 'N', 'M']
number = ['0', '1','2', '3','4', '5','6', '7','8', '9']
if alphabet in alpha:
    print(alphabet, " is an alphabet.")
elif alphabet in number:
    print(alphabet, " is a number.")
else:
    print(alphabet, " is a special character.")