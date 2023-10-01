# retrieve input from the user
num = int(input("Enter a number: "))

''' use modulus to calculate if there is a remainder when dividing by 2 to 
see if input is even '''
if num % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
