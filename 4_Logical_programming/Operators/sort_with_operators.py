# declare three variables
num1 = 544
num2 = 9999
num3 = 777

# display the larger value of num1 and num2
if num1 > num2:
    print(f"{num1} is larger than {num2}")
else:
    print(f"{num2} is larger than {num1}")

# determine whether num1 is odd or even and display the result
if num1 % 2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

# use conditional statements to sort the three numbers from largest to smallest
if num1 > num2 and num1 > num3:
    largest = num1
    if num2 > num3:
        middle = num2
        smallest = num3
    else:
        middle = num3
        smallest = num2
elif num1 < num2 and num1 < num3:
    smallest = num1
    if num3 > num2:
        largest = num3
        middle = num2
    else:
        largest = num2
        middle = num3
else:
    middle = num1
    if num2 > num3:
        largest = num2
        smallest = num3
    else:
        largest = num3
        smallest = num2

# print the result
print(f"From largest to smallest, the numbers are {largest}, {middle}, {smallest}")
