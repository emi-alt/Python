tup = (2,3,4,5,6)
prod = []
def mul():
    for m in tup:
        m *= 2
        prod.append(m)
mul()
p = tuple(prod)
print(type(p))
print(p)