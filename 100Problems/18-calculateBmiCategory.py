# Calculate BMI 
# BMI = weight (kg) / height (m)^2
# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: ")) 
if weight <= 0:
    print("Weight must be a positive number.")
    exit()
height = float(input("Enter your height in meters: "))
if height <= 0:
    print("Height must be a positive number.")
    exit()
# Calculate BMI
bmi = weight / (height ** 2)
# Print the result
print(f"Your BMI is: {bmi:.2f}") 

# output
# Enter your weight in kilograms: 76
# Enter your height in meters: 1.7
# Your BMI is: 26.30