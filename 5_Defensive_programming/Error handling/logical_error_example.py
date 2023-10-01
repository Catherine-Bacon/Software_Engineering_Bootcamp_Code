# write a program that displays a logical error (be as creative as possible!)

# calculate how many days until Christmas

# retrieve inputs from user
day = int(input("What is the day of the month?: "))
month = int(input("What number month is it in the year?: "))

# calculate days until Christmas
day_of_year = (month * 30) + day
num_days = 359 - day_of_year

# print output to user
print(f"There are {num_days} days until Christmas!")

# logical errors:
# code only takes into account years with 365 days
# code does not take into account months with non-30 days

