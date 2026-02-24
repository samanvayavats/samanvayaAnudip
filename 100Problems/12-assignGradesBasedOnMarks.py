# 12-assignGradesBasedOnMarks

marks = int(input("Enter the  marks: "))

if marks>=90 and marks<=100:
    print('A+ Grade')
elif marks>=80 and marks<90:
    print('A Grade')
elif marks>=70 and marks<80:
    print('B+ Grade')
elif marks>=60 and marks<70:
    print('B Grade')
elif marks>=50 and marks<60:
    print('c+ Grade')
elif marks>=40 and marks<50:
    print('c Grade')
else:
    print('E Grade')

# output
# Enter the  marks: 45
# c Grade
