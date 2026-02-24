# 26-checkArmstrongNumber
number = int(input("Enter the number: "))
if number<0:
  print("Armstrong number is not defined for negative numbers.")
  exit()
# Store the original number for later use
num = number
# Initialize the variable to store the sum of the cubes of the digits
armstrong_sum = 0
degit_count = 0
# Calculate the sum of the cubes of the digits using a while loop
while number != 0:
    degit_count += 1
    number //= 10
number = num  # Reset number to the original value
while number != 0:
    digit = number % 10  # Get the last digit
    armstrong_sum += digit ** degit_count  # Add the cube of the digit to the sum
    number //= 10  # Remove the last digit from the original number
# Check if the sum of the cubes of the digits is equal to the original number
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
# output
# Enter the number: 153
# 153 is an Armstrong number.