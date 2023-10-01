# save sentence as a string
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# print with "!" replaced with spaces
print(string.replace("!", " "))

# print in all uppercase; requires a new variable
sentence = string.replace("!", " ")
print(sentence.upper())

# print the reversed sentence
print(sentence[::-1])
