# retrieve user inputs
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

# calculate the user's BMI and establish weight range variable
BMI = weight/height**2
weight_range = ""

# calculate weight range from the BMI
if BMI >= 30:
    weight_range += "obese"
elif BMI >= 25:
    weight_range += "overweight"
elif BMI >= 18.5:
    weight_range += "normal"
else:
    weight_range += "underweight"

# display results to user
print(f"Your BMI is {BMI:.2f}, which means you are {weight_range}.")
