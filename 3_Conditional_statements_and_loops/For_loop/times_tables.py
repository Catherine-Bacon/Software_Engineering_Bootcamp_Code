# retrieve input from user
num = int(input("Enter a number: "))

# create for loop calculating and displaying input multiplied by numbers up to 12
print(f"The {num} times table is:")
for i in range(1, 13):
    print(f"{num} * {i} = {num * i}")
