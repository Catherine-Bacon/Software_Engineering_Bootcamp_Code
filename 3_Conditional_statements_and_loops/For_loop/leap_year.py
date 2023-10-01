# retrieve input from user
year = int(input("Enter the year you want to start with: "))
num_years = int(input("How many years do you want to check? "))

# check if years are divisible by 4 (a leap year), iterating using a for loop the inputted number of times
for i in range(0, num_years):
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} isn't a leap year")
    year += 1
