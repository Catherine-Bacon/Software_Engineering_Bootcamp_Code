# initialise vowel counting variable
vowel_count = 0

# open text file and convert to a list and a string
with open('input.txt', 'r') as f:
    content_list = f.readlines()
    content_string = "".join(content_list).replace("\n", "").lower()

    # count the number of characters, words and lines
    character_count = len(content_string.replace(" ", ""))
    word_count = len(content_string.split(" "))
    line_count = len(content_list)

    # iterate through string, adding one to the vowel count for every vowel found
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(content_string)):
        if content_string[i] in vowels:
            vowel_count += 1

# print the results
print("In your text file there are:")
print(f"{character_count} characters")
print(f"{word_count} words")
print(f"{line_count} lines")
print(f"{vowel_count} vowels")
