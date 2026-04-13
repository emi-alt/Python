def pel(words):
    ctr = 0
    lis = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lis.append(word)
    print("The words that have the same first and last letter same are: ", lis)
    print(f"There are {ctr} such words in the list.")

pel(["otto", "mango", "car", "mom", "dad", "1221", "454", "90879"])