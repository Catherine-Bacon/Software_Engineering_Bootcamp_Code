# retrieve initial input from user
num = int(input("Enter a number less than or equal to 100: "))

# whilst the input is above 100, repeatedly re-ask the input question
while num > 100:
    print("Please try again")
    num = int(input("Enter a number less than or equal to 100: "))

# multiply even numbers by 2 and odd numbers by 3; display the result
if num % 2 == 0:
    print(f"Your number multiplied by 2 is {num*2}")
else:
    print(f"Your number multiplied by 3 is {num*3}")
