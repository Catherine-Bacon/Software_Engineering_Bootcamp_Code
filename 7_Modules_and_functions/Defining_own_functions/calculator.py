# define functions
def add_num(num1, num2):
    # adds two inputs together
    return num1 + num2


def subtract_num(num1, num2):
    # subtracts first input from the second
    return num1 - num2


def multiply_num(num1, num2):
    # multiplies two inputs together
    return num1 * num2


def divide_num(num1, num2):
    # divides first input by the second input
    return num1 / num2


# print menu to user and retrieve valid input using while loop
print("""CALCULATOR:
 1 - add
 2 - subtract
 3 - multiply
 4 - divide""")
while True:
    x = int(input("\nEnter your choice's number: "))
    if x in [1, 2, 3, 4]:
        break
    print("Incorrect input, try again.")

# use input to perform relevant function; asking for function inputs where relevant and printing the result
if x == 1:
    add_input_1 = int(input("Enter a number: "))
    add_input_2 = int(input("Enter another number: "))
    print(f"{add_input_1} + {add_input_2} = {add_num(add_input_1, add_input_2)}")
elif x == 2:
    subtract_input_1 = int(input("Enter a number: "))
    subtract_input_2 = int(input("Enter a number to take away: "))
    print(f"{subtract_input_1} - {subtract_input_2} = {subtract_num(subtract_input_1, subtract_input_2)}")
elif x == 3:
    multiply_input_1 = int(input("Enter a number: "))
    multiply_input_2 = int(input("Enter another number: "))
    print(f"{multiply_input_1} * {multiply_input_2} = {multiply_num(multiply_input_1, multiply_input_2)}")
else:
    divide_input_1 = int(input("Enter a number to be divided: "))
    divide_input_2 = int(input("Enter the dividing number: "))
    print(f"{divide_input_1} / {divide_input_2} = {divide_num(divide_input_1, divide_input_2)}")
