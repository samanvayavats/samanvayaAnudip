# 15-divisibleBy3And5

a = int(input('enter the number '))

if (a%3 == 0 and a%5 ==0 ):
    print(f"{a} is divisible by both")
else:
    print(f"{a} is not divisible by both")

# output
# enter the number 9
# 9 is not divisible by both