# to create a list 20 numbers and ask the user to input any number and delete this number from the list from its all the occurences except the 
# first occurence 

numberList = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,]
count = True
userNumber =int(input('enter the number which u want to remove from the list '))
numberList.reverse()

if userNumber in numberList:
    for i in numberList:
        if(i == userNumber and count==True):
            count=False
        else:
            if(i==userNumber and count==False ):
                numberList.remove(userNumber)

else:
    print('number not exits')

numberList.reverse()
print(numberList)