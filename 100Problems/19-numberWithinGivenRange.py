# 19-numberWithinGivenRange
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
number = int(input("Enter the number: "))
# Check for lies in the range
if number >= start and number <= end:
    print("Number is lies in the given range")
else:
    print("Number does n't lies with in the given range")

# output
# Enter the starting number: 10
# Enter the ending number: 50
# Enter the number: 20
# Number is lies in the given range