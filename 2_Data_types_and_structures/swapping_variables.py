# retrieve two numbers from the user and store them in variables
num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")

# print the numbers before the swap
print(f"Before the swap num1 equalled {num1}")
print(f"Before the swap num2 equalled {num2}")

# swap the numbers around, i.e. num1 to num2 and num2 to num1
''' i learnt this method through https://www.programiz.com/python-programming/examples/swap-variables
    i used the method without a temporary variable for efficiency '''
num1, num2 = num2, num1

# print out the values for num1 and num2
print(f"After the swap num1 equals {num1}")
print(f"After the swap num2 equals {num2}")

