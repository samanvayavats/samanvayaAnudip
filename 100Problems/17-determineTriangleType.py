# 17-determineTriangleType
# Determine the type of triangle based on the lengths of its sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
# Validating the sides to ensure they are positive
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Sides of a triangle must be positive.")
    exit()
# Check if the sides can form a triangle using the triangle inequality theorem
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is an isosceles triangle.")
    else:
        print("The triangle is a scalene triangle.") 