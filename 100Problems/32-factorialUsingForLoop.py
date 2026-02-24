# 32-factorialUsingForLoop
num = int(input("Enter the number: "))
# Validate the number is not a negative number
if num < 0:
    print("can not find the factorial of the negative number")
fact = 1
# Evaluate the factorial
for i in range(1, num + 1):
    fact *= i
# Print the result
print(f"Factorial of {num} is {fact}")

# output 
# Enter the number: 4
# Factorial of 4 is 24