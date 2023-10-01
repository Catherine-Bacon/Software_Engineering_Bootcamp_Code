# retrieve input from user and change it to an all lowercase list
word = list(input("Enter a word and we'll return the number of times each character occurs: ").lower())

# create empty dictionary
character_occurrence = {}

# iterate through the input, adding one for each letter's respective key,
# or adding the letter as a key with value one if not found; print the resulting dictionary
for i in word:
    character_occurrence[i] = character_occurrence.get(i, 0) + 1
print(f"Each character's occurrence is {character_occurrence}")
