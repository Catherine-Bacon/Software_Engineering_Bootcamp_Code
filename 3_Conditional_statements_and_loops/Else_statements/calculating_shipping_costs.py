# retrieve inputs from user (allow them to input decimals)
price = float(input("Enter the price (R) of the item you want to purchase: "))
distance = float(input("Enter the total distance (km) of the delivery: "))

travel = input("Will the parcel be delivered by air or freight? (a/f) ").lower()
insurance = input("Will you get full or limited insurance? (f/l) ").lower()
gift = input("Is this a gift? (y/n) ").lower()
delivery = input("Is the delivery priority or standard? (p/s) ").lower()

# initialise cost and error variables
cost = price
error = 0

#calculate individual costs
if travel == "a":
    cost += 0.36 * distance
elif travel == "f":
    cost += 0.25 * distance
else:
    print("Incorrect mode of travel input (a/f)")
    error += 1

if insurance == "f":
    cost += 50
elif insurance == "l":
    cost += 25
else:
    print("Incorrect insurance input (f/l)")

if gift == "y":
    cost += 15
elif cost == "n":
    cost += 0
else:
    print("Incorrect gift option added (y/n)")

if delivery == "p":
    cost += 100
elif delivery == "s":
    cost += 20
else:
    print("Incorrect delivery option added (p/s)")

# calculate total cost sending the parcel and produce error message for incorrect inputs
if error == 0:
    print(f"The total cost of sending the parcel is R{cost:.2f}")
else:
    print("Please retry and only respond with single letter responses")
