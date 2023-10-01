# import module
from statistics import median

# create a list and put inputs into the list
floats = []
for i in range(5):
    num = float(input("Input a float: "))
    floats.append(num)

# calculate the total, average (using total), and median
total = sum(floats)
average_2_dp = round(total / len(floats), 2)
median = median(floats)

# calculate the max and min number's indexes
max_index = floats.index(max(floats))
min_index = floats.index(min(floats))

# print results to user
print(f"\nThe total of the numbers is {total}")
print(f"The index of the maximum number is {max_index}")
print(f"The index of the minimum number is {min_index}")
print(f"The average of the numbers to 2 d.p. is {average_2_dp}")
print(f"The median number is {median}")
