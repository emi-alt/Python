print("Finding LCM of two numbers.")
num_big = int(input("Enter the larger number: "))
num_smol = int(input(f"Enter the smaller number: "))
HCF = num_big
b = num_smol

while(b > 0):
  num_store = b
  b = HCF % b
  HCF = num_store
print(f"HCF of {num_big} and {num_smol} is {HCF}")
#num_big = hcf
lcm = (num_big * num_smol) // HCF
print(f"LCM of {num_big} and {num_smol} is {lcm}")