# retrieve inputs from the user
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter a different integer: "))
int3 = int(input("Enter a different integer number: "))

''' calculate the sum of all three, the first number minus the second, the third 
    multiplied by the first and then the sum of all three divided by the third '''
sum = int1 + int2 + int3
first_minus_second = int1 - int2
third_times_first = int3 * int1
sum_over_third = sum / int3

# print the results
print(f"The sum of all three is {sum}")
print(f"First number minus the second is {first_minus_second}")
print(f"Third number multiplied by the first is {third_times_first}")
print(f"Sum divided by the third is {sum_over_third}")
