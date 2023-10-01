# import required module
import math

# retrieve inputs from the user
side1 = float(input("Enter the length of one side of the triangle: "))
side2 = float(input("Enter the length of another side of the triangle: "))
side3 = float(input("Enter the length the final side of the triangle: "))

# calculate the area of the triangle using Heron's formula
half_perimeter = 0.5 * (side1 + side2 + side3)
area = math.sqrt(half_perimeter * (half_perimeter - side1) * (half_perimeter - side2) * (half_perimeter - side3))

# display the result
print(area)

