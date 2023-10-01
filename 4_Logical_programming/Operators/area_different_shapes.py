# import modules
import math

# retrieve inputs from the user
shape = input("Is your building square, rectangular or round? ").lower()

# prompt for appropriate dimensions, calculation and display of areas to 2 dp
# and display if incorrect house shape is inputted
if shape == "square":
    length = float(input("What is the length of house's side in metres? "))
    area = length ** 2
    print(f"Your house's area is {area:.2f} metres squared")
elif shape == "rectangular":
    length = float(input("What is the house's length in metres? "))
    width = float(input("What is the house's width in metres? "))
    area = length * width
    print(f"Your house's area is {area:.2f} metres squared")
elif shape == "round":
    radius = float(input("What is the house's radius in metres? "))
    area = math.pi * radius ** 2
    print(f"Your house's area is {area:.2f} metres squared")
else:
    print("You have entered an incorrect house shape, please try again")
