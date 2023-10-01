# define functions:
def hotel_cost(num_nights):
    # returns hotel cost from the number of nights the user is staying there (input) and a preset price per night
    price_per_night = 40
    hotel = num_nights * price_per_night
    return hotel


def plane_cost(city):
    # returns the price of a flight from the city the user is flying to (input)
    city = city.lower()
    if city == "london":
        plane = 200
    elif city == "new york":
        plane = 400
    elif city == "paris":
        plane = 350
    else:
        plane = 0
    return plane


def car_rental(days_hired):
    # returns car rental cost from the number of days the car is being rented (input) and a preset price per day
    price_per_day = 20
    car = days_hired * price_per_day
    return car


def holiday_cost(num_nights, city, days_hired):
    # returns the total holiday costs using hotel_cost, plane_cost and car_rental functions
    total = hotel_cost(num_nights) + plane_cost(city) + car_rental(days_hired)
    return total


# retrieve inputs from user
num_nights_input = int(input("Enter the number of nights you will be staying at the hotel: "))
city_input = input("Enter the city you are flying to (london, new york or paris): ")
days_hired_input = int(input("Enter the number of days you will be hiring a car: "))

# enter inputs into functions and save results as variables
hotel_output = hotel_cost(num_nights_input)
plane_output = plane_cost(city_input)
car_output = car_rental(days_hired_input)
total_output = holiday_cost(num_nights_input, city_input, days_hired_input)

# print outputs to user, accounting for incorrect flight destination possibility
print(f"\nYour hotel will cost £{hotel_output}")
print(f"Your car rental will cost £{car_output}")
if plane_output == 0:
    print("\tERROR: Incorrect input for flight destination")
    print(f"The total cost of the holiday without the flight is £{total_output}")
else:
    print(f"Your flight will cost £{plane_output}")
    print(f"The total cost of the holiday is £{total_output}")
