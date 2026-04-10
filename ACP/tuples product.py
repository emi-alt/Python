tup = (2,3,4,5,6)

def mult(p):
    while len(tup)>0:
     if p in tup:
        p *= 1
        return p
print(mult(tup))