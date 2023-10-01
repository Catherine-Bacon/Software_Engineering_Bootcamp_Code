# retrieve user input (sentence)
str_manip = input("Enter a sentence: ")

# calculate and display the string length
print(len(str_manip))

# find the last letter of the input and replace every occurrence of this with @
print(str_manip.replace(str_manip[-1], "@"))

# print the last three letters of the input backwards
print(str_manip[-1:-4:-1])

# create a five-letter word made of the first three and last two characters of the input
first_three = str_manip[0:3:1]
last_two = str_manip[-2:len(str_manip):1]
print(f"{first_three}{last_two}")

# display each word on a new line
print(str_manip.replace(" ", "\n"))
