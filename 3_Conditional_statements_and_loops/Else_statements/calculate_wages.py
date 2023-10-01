# retrieve inputs from the user
employee = input("Are you a salesperson or manager? (s/m) ").lower()

# calculate wage for each employee type and setup error message
# print wage to 2 decimal places
if employee == "s":
    gross_sales = float(input("What are your gross sales for this month? "))
    wage = 2000 + gross_sales * 0.08
    print(f" Your wage for this month is R{wage:.2f}")
elif employee == "m":
    hours = float(input("How many hours have you worked this month? "))
    wage = 40 * hours
    print(f"Your wage for this month is R{wage:.2f}")
else:
    print("Your input is wrong, please retry and only enter s/m.")
