# 29-gcdUsingWhileLoop
number1 = int(input("Enter the number1: "))
# validate that first number is positive or not
if number1 < 0:
    print("GCD is not defined for negative value")
    exit()
number2 = int(input("Enter the number2: "))
# validate that second number is not zero
if number2 < 0:
    print("GCD is not defined for negative value")
    exit()
# Find the minimum of the two numbers to limit the range for finding GCD
min_value = min(number1, number2)
gcd = 1
# Calculate GCD using a for loop
for i in range(1, min_value + 1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
# Print the result
print("GCD is:", gcd)

# output
# Enter the number1: 4
# Enter the number2: 8
# GCD is: 4