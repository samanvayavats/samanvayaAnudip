# Count the digit in a number
number = int(input("Enter a number(digit must be positive number): "))
if number < 0:
    print("Negative numbers are not supported.")
    exit()
# Store the original number for later use
num = number
# Initialize the variable to store the count of digits
digit_count = 0
# Count the digits using a while loop
while number != 0:
    number //= 10  # Remove the last digit from the number
    digit_count += 1  # Increment the digit count
# Print the result
print(f"The number of digits in {num} is: {digit_count}.")

# output
# Enter a number(digit must be positive number): 134
# The number of digits in 134 is: 3.