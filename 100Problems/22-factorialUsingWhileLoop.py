# 22-factorialUsingWhileLoop
number = int(input("Enter the number: "))
# Store the original number for later use
num = number
# Check if the number is negative, zero, or positive and calculate factorial accordingly
if number<0:
  print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
  print(f"The factorial of {number} is 1.")
else:
  factorial = 1
  # Calculate factorial using a while loop
  while(number > 1):
    factorial *= number
    number -= 1
  # Print the result
  print(f"The factorial of {num} is {factorial}.")


# output
# Enter the number: 4
# The factorial of 4 is 24.