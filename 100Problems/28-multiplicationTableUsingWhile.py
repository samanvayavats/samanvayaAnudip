# 28-multiplicationTableUsingWhile

number = int(input("Enter the number: "))
# Validate that number is positive or not
if number<0:
  print("Table is not defined for negative number")
  exit()

for num in range(11):
  print(f"{number}X{number}={num*number}")

# output
# Enter the number: 4
# 4X4=0
# 4X4=4
# 4X4=8
# 4X4=12
# 4X4=16
# 4X4=20
# 4X4=24
# 4X4=28
# 4X4=32
# 4X4=36
# 4X4=40