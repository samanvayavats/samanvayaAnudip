# 27-fibonacciUsingWhileLoop
n = int(input("Enter the number of terms in the Fibonacci series: "))
# Store the original number for later use
num = n
# Initialize the first two terms of the Fibonacci series
a, b = 0, 1
# Generate the Fibonacci series using a while loop
print("Fibonacci series:")
while n > 0:
    print(a, end=' ')
    a, b = b, a + b  # Update the values of a and b
    n -= 1  # Decrement the term count
# Print a newline after the series
print()
# output
# Enter the number of terms in the Fibonacci series: 10
# Fibonacci series:
# 0 1 1 2 3 5 8 13 21 34
