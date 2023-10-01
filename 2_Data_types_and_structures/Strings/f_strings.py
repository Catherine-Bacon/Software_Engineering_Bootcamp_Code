# retrieve information from the user, with relevant data types
name = input("Enter your name: ")
age = int(input("Enter your age: "))
house_number = int(input("Enter your house number: "))
street_name = input("Enter your street name: ")

# print out a single sentence containing all the details of the user
print(f"This is {name}, they are {age} years old and live at house number {house_number} on {street_name}.")
