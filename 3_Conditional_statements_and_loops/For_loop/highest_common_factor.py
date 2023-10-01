# while loop counting down from 20 to 0
num = 20
while num >= 0:
    print(num)
    num -= 1
print("")

# for loop printing even numbers in range 1 to 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
print("")

# for loop printing the star variable for 5 iterations, with each iteration adding another asterisk to the variable
star = "*"
for i in range(5):
    print(star)
    star += "*"
print("")

# retrieve inputs from user
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

# find the smallest input
if int1 < int2:
    smaller = int1
else:
    smaller = int2

# test whether inputs are divisible by the smaller input, then by the next lowest number (-1) and so on
# when both integers are divisible by the number, the loop breaks and prints this number (hcf)
for i in range(smaller + 1, 0, -1):
    if (int1 % i == 0) and (int2 % i == 0):
        print(f"{i} is the highest common factor of {int1} and {int2}")
        break
