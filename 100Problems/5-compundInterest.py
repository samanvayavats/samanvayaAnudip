# Problem 5
# Problem Statement: Calculate compound interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply

principle = float(input("Enter the principle: ") )
rate = float(input("Enter the rate of interest: ") )
time = float(input("Enter the time: "))

amount = principle * (pow((1 + rate / 100), time))
ci = amount - principle

print("Compound interest is", ci)

# output
# Enter the principle: 1000
# Enter the rate of interest: 5
# Enter the time: 3
# Compound interest is 157.62500000000023