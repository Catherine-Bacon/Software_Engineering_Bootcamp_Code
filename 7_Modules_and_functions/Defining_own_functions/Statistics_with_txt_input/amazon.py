# input file (input_for_amazon_with_optional_task.txt) has been uploaded to dropbox with the extra inputs
# import math module for ceil
import math


# define functions
def minimum(list1):
    # returns minimum value in a list of integers
    return min(list1)


def maximum(list2):
    # returns maximum value in a list of integers
    return max(list2)


def average(list3):
    # returns average of a list of integers
    return sum(list3) / len(list3)


def percentile(percent, list_of_values):
    # returns the rounded up index of a desired value within a list (input) from its percentile (input)
    num_in_list = math.ceil((percent / 100) * len(list_of_values))
    return num_in_list


def summation(list4):
    return sum(list4)


# open input file and read to a variable; create empty list
with open('input_for_amazon.txt', 'r', encoding='utf-8-sig') as f:
    content = f.readlines()
output_lines = []

# for each line, determine what function to perform, strip unwanted characters, split into a list,
# cast to integers, then perform the relevant function and add the result to the output_lines variable.
# for percentile, retrieve percentile value from string to use in function
for line in content:
    if line[0:3] == "min":
        min_list = line.strip("min: \n").split(",")
        min_list = [int(x) for x in min_list]
        output_lines.append(f"The min of {min_list} is {minimum(min_list)}")
    elif line[0:3] == "max":
        max_list = line.strip("max: \n").split(",")
        max_list = [int(x) for x in max_list]
        output_lines.append(f"The max of {max_list} is {maximum(max_list)}")
    elif line[0:3] == "avg":
        avg_list = line.strip("avg: \n").split(",")
        avg_list = [int(x) for x in avg_list]
        output_lines.append(f"The avg of {avg_list} is {average(avg_list)}")
    elif line[0:3] == "sum":
        sum_list = line.strip("sum: \n").split(",")
        sum_list = [int(x) for x in sum_list]
        output_lines.append(f"The sum of {sum_list} is {summation(sum_list)}")
    else:
        per_list = line
        percent_val = int(per_list[1:3])
        per_list = per_list.strip(f"p{percent_val}: \n").split(",")
        per_list = [int(x) for x in per_list]
        output_lines.append(f"The {percent_val}th percentile of {per_list} is {percentile(percent_val, per_list)}")

# join the output_lines variable and print resulting string to an output file
output_string = "\n".join(output_lines)
with open('output_for_amazon.txt', 'w') as f:
    f.write(output_string)
