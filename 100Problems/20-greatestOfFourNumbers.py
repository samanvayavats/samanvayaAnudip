# 20-greatestOfFourNumbers
a = 0
arr =[]
while True:
    ptr = int(input('enter the number '))
    arr.append(ptr)
    if(a==3): break
    a+=1

temp = 0

for i in arr:
    if temp<i:
        temp=i

print(f"{temp} is greatest among four .")

# ouput
# enter the number 1
# enter the number 2
# enter the number 3
# enter the number 4
# 4 is greatest among four .