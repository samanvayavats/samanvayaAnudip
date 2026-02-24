# 9-sumOfDigits

a= int(input('enter the number '))
sum = 0 
while(a):
    rem = a%10
    sum+=rem
    a=a//10

print('the sum of digit is ' , sum)

# output
# enter the number 1234
# the sum of digit is  10