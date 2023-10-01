# create empty list to contain numbers
nums = []

# retrieve numbers from user (added to the numbers list) and create a break condition
while True:
    num = int(input("Enter a number, or -1 if you want the average of numbers entered: "))
    if num == -1:
        break
    nums.append(num)

# calculate and display the average of the numbers
average = sum(nums)/len(nums)
print(f"The average of the numbers entered is {average}")
