# instantiate variables
clean_car_red = True
clean_car_blue = True
clean_car_green = True
num_of_car = 0
busy = False
car_colours = ["Red", "Blue", "Green"]

print("Welcome to the car wash")

for colour in car_colours:
    dirty_check = input(f"Is the {colour} car Dirty? (Yes or No): ")
    if dirty_check == "Yes":
        print(f"{colour} car really needs a cleaning")
        clean_car_red = False
        num_of_car += 1

if num_of_car == 3:
    busy = True

if busy:
    print("\nThe car wash was packed today")
