# retrieve input from user
num = int(input("Enter a number: "))

# declare control variable
i = 1

# form while loop to print even numbers, and add one to control variable until it reaches the num value
print("The even numbers from 1 up until and including your number are:")
while i <= num:
    if i % 2 == 0:
        print(i)
    i += 1
