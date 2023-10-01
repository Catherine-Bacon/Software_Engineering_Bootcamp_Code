# retrieve input from user and form empty list
name = input("Enter your name: ")
incorrect_names = []

# while loop to add non-John inputs to list and re-ask for input
while name.lower() != "john":
    incorrect_names.append(name)
    name = input("Enter your name: ")

# print non-john names once john is inputted
print(f"Incorrect names: {incorrect_names}")
