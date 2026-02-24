# Problem 4
# Problem Statement: Calculate simple interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

principle = int(input('enter the principle '))
rate = int(input('enter the rate '))
interest = int(input('enter the interest '))

simple  = (principle*rate*interest)/100

print('the simple interest is ' , simple)

# output
# enter the principle 10000
# enter the rate 5
# enter the interest 3
# the simple interest is  1500.0