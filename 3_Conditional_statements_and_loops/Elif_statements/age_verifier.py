# retrieve user input
age = int(input("Enter your age: "))

# setup if statement and print relevant message for each range
if age >= 18:
    print("You are old enough!")
elif age > 16:
    print("Almost there.")
else:
    print("You're just too young!")

