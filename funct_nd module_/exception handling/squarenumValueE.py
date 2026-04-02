try:
  n = int(input("Enter a number: "))
  def square():
   return n*n
  print(square())
except:
  print("Something went wrong.")
print("outside except")