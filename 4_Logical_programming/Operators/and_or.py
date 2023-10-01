# retrieve input from the user
num = int(input("Enter an integer: "))

# determine divisibility of number and print result
if num % 2 == 0 and num % 5 == 0:
    print("Your number is divisible by 2 and 5.")
elif num % 2 == 0 or num % 5 == 0:
    print("Your number is divisible by 2 or 5.")
else:
    print("Your number is not divisible by 2 or 5.")
