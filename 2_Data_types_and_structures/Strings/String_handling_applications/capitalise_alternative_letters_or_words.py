# retrieve input from user and create empty string
string = "Hello World"
funky_string = ""

# create for loop iterating through string, capitalising every other character
for i in range(len(string)):
    if i % 2 == 0:
        funky_string += string[i].upper()
    else:
        funky_string += string[i].lower()

# print created string
print(funky_string)

# split string into a list, and create empty list
string = "I am learning to code"
split_string = string.split()
funky_sentence = []

# capitalise every other word and add these to the empty list
for word in range(len(split_string)):
    if word % 2 == 0:
        funky_sentence.append(split_string[word].lower())
    else:
        funky_sentence.append(split_string[word].upper())
# join the list and print
funky_sentence = " ".join(funky_sentence)
print(funky_sentence)
