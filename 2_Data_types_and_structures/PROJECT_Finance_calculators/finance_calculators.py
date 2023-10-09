# Import required module
import math

# Print information to the user about investments and bonds, and let the user choose the relevant calculator.
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")
calculation_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Retrieve inputs for investment, then calculate and output the appropriate amount they will get back during
# the given period for their investment type, and setup interest type error.
if calculation_type == "investment":
    deposit = float(input("\nEnter the amount of money you are depositing in £: "))
    interest_rate = float(input("Enter your annual interest rate (without '%'): ")) / 100
    years = float(input("Enter the number of years you plan on investing: "))
    interest_type = input("Do you want 'simple' or 'compound' interest? ").lower()
    if interest_type == "simple":
        interest = deposit * (1 + interest_rate * years)
        print(f"\nYou will receive £{interest:.2f} after {years} years at an interest rate of {interest_rate * 100}%.")
    elif interest_type == "compound":
        interest = deposit * math.pow((1 + interest_rate), years)
        print(f"\nYou will receive £{interest:.2f} after {years} years at an interest rate of {interest_rate * 100}%.")
    else:
        print("\nIncorrect interest type entered, please retry and enter 'simple' or 'interest'.")

# Retrieve inputs for bond, then calculate and output the appropriate amount they will have to pay each month
elif calculation_type == "bond":
    house_value = float(input("\nEnter the present value of your house in £: "))
    monthly_interest_rate = float(input("Enter your annual interest rate (without '%'): ")) / (100 * 12)
    months = float(input("Enter the number of months you plan to take to repay the bond: "))
    repayment = (monthly_interest_rate * house_value)/(1 - math.pow((1 + monthly_interest_rate), -months))
    print(f"\nYou will have to repay £{repayment:.2f} each month for {months} months.")

# Form else statement in case of incorrect calculation_type input
else:
    print("\nIncorrect calculation type entered, please retry and enter 'investment' or 'bond'.")
