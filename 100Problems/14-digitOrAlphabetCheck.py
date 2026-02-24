# 14-digitOrAlphabetCheck

temp = input('enter the input ')

if(temp.isalpha()):
    print(f"{temp} is alphabet")
elif(temp.isdigit()):
    print(f"{temp} is digit")
else:
    print(f"{temp} is digit not alphabet")

# output
# enter the input 1
# 1 is digit