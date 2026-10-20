SECRET_CODE = 17
ACCESS_KEY = 46

def bit_scanner():
    format(SECRET_CODE, '08b')

bit_scanner()

print(f"Secret code in binary is: {bin(SECRET_CODE)}")
print(f"Access key in binary is: {bin(ACCESS_KEY)}")

print(f" AND operation on {SECRET_CODE} and {ACCESS_KEY}:\n{bin(SECRET_CODE & ACCESS_KEY)}")
print(f" OR operation on {SECRET_CODE} and {ACCESS_KEY}:\n{bin(SECRET_CODE | ACCESS_KEY)}")

print(f" NOT operation on {SECRET_CODE}:\n{bin(~SECRET_CODE)}")
print(f" NOT operation on {ACCESS_KEY}:\n{bin(~ACCESS_KEY)}")
print(f" XOR operation on {SECRET_CODE} and {ACCESS_KEY}:\n{bin(SECRET_CODE ^ ACCESS_KEY)}")
print(f" XOR operation on {ACCESS_KEY} and {SECRET_CODE}:\n{bin(ACCESS_KEY ^ SECRET_CODE)}")

print(f"Left shift operation:\n{SECRET_CODE} << 1 = {bin(SECRET_CODE << 1)}")
print(f"Right shift operation:\n{SECRET_CODE} >> 1 = {bin(SECRET_CODE >> 1)}")
print(f"Left shift operation:\n{ACCESS_KEY} << 1 = {bin(ACCESS_KEY << 1)}")
print(f"Right shift operation:\n{ACCESS_KEY} >> 1 = {bin(ACCESS_KEY >> 1)}")

EorO = SECRET_CODE ^ 1
if EorO == SECRET_CODE + 1:
    print(f"{EorO} is an even number.")
    print(f"therefore, {SECRET_CODE} is an even number.")
else:
    print(f"{SECRET_CODE} is an odd number.")

def bit_count(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
count = bit_count(SECRET_CODE)
print(f"The number of 1s in the binary representation of {SECRET_CODE} is: {count}")