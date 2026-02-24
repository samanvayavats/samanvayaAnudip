# Problem 3
# Problem Statement: Find the largest of three numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

a = int(input('enter the first number '))
b = int(input('enter the second number '))
c = int(input('enter the third number '))

if a > b:
    if a>c:
        print('first number is greater')
    else:
        print('third number is greater')
else:
    if b>c:
        print('second number is greater')
    else:
        print('third number is greater')


# output
# enter the first number 1
# enter the second number 2
# enter the third number 3
# third number is greater