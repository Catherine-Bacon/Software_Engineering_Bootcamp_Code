### ASSIGNMENT:

Create a **function to produce statistics**, which takes in a .txt file which lists instructions e.g. min and integers e.g. 1,2,3,4,5,6 and produces the instruction's output in an outputted txt file.

For example, if the input.txt file has the following:\
min: 1,2,3,5,6\
max: 1,2,3,5,6\
avg: 1,2,3,5,6\
p90: 1,2,3,4,5,6,7,8,9,10\
sum: 1,2,3,5,6\
min: 1,5,6,14,24\
max: 2,3,9\
p70: 1,2,3

Your output.txt should read:\
The min of [1, 2, 3, 5, 6] is 1\
The max of [1, 2, 3, 5, 6] is 6\
The avg of [1, 2, 3, 5, 6] is 3.4\
The 90th percentile of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 9\
The sum of [1, 2, 3, 5, 6] is 17\
The min of [1, 5, 6, 14, 24] is 1\
The max of [2, 3, 9] is 9\
The 70th percentile of [1, 2, 3] is 2