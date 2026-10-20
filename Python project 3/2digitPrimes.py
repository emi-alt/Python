from math import sqrt
prime = []
print("The 2 digit prime numbers are, ")
for num in range(10, 100):
    if num > 1:
        for i in range(2, int((sqrt(num))+1)):
            if (num % i) == 0:
                break
        else:
            prime.append(num)
            print(num, end=" ")
            print()
print(f"There are total {len(prime)} 2-digit prime numbers")