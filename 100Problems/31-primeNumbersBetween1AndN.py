# 31-primeNumbersBetween1AndN

number = int(input("Enter the range: "))
# Validate the range is not a negative value
if number < 0:
    print("Prime number is not defined for negative range")
    exit()


# Create a is_prime_num to check the number is prime or not
def is_prime_num(n):
    for i in range(2, n):
        # Checks if the number is divided by any value between the 2 and number then returns the false
        if n % i == 0:
            return False

    return True


# Print result
for i in range(1, number + 1):
    if is_prime_num(i):
        print(i, end=" ")

# output
# Enter the range: 4
# 1 2 3 