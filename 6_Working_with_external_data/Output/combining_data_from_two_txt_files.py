# create two files with integers in ascending order and create variables storing data
with open('numbers1', 'w+') as f:
    f.write("1 5 8 10 12")
    f.seek(0)
    num_1 = f.readlines()
with open('numbers2', 'w+') as f:
    f.write("2 4 7 11 13")
    f.seek(0)
    num_2 = f.readlines()

# join data variables and create list
nums = " ".join(num_1 + num_2).split(" ")

# convert elements in list to integers and sort
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()

# convert sorted list to a string and write to file
num_string = " ".join(str(i) for i in nums)
with open('all_numbers', 'w') as f:
    f.write(num_string)
