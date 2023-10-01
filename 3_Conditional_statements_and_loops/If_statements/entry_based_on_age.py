# retrieve input from the user
year = int(input("What year were you born? "))

# calculate age from the input
age = 2022 - year

# form an if statement to tell user if they can enter the party
if age >= 18:
    print("Congrats you are old enough.")