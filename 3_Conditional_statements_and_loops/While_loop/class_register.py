# create empty list to contain names
names = []

# retrieve names from user (added to the names list) and create a break condition
while True:
    name = input("Enter a pupil's name, or enter 'stop' when all student names have been entered: ").lower()
    if name == "stop":
        break
    names.append(name)

# print the number of names entered (length/no. elements in list)
print(f"You entered {len(names)} names.")
