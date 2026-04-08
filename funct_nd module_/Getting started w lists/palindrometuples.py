def palin(w):
    e = len(w) - 1
    s = 0
    while (s<e):
        if w[s] != w[e]:
            return False
        s += 1
        e -= 1
        return True

w = (3,4,5,4,2)

if palin(w):
    print("This tuple is a palindrome.")
else:
    print("This tuple is not a palindrome.")