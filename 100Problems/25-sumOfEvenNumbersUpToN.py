# 25-sumOfEvenNumbersUpToN

number = int(input("Enter a number(digit must be positive number): "))
sum = 0 

for i in range(0 , number+1):
    if i%2==0:
        sum+=i

print(f'the sum of even number is {sum}')

# ouput
# Enter a number(digit must be positive number): 4
# the sum of even number is 6