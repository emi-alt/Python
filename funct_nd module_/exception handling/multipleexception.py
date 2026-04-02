try:
 num1, num2 = eval(input("Enter two integers separated by commas: "))
 result = num1/num2
 print("The result is ", result)

except ZeroDivisionError:
  print("Divison by zero is not possible.")
except SyntaxError:
  print("Comma is missing. Please enter two integers separated by commas, like 1, 2")
except ValueError:
  print("Wrong input. Please enter a number.")
except:
  print("Something went wrong.")
else:
  print("No exception.")
finally:
  print("This will print no matter what.")