def cube(num):
    return num*num*num

def by_3(num):
    if num%3 == 0:
        return cube(num)
    else:
        return False
print(by_3(3))
print(by_3(5))