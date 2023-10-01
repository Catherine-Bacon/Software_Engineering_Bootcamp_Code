# retrieve user input
sentence = input("Enter a sentence: ")
strip_letters = []

while True:
    letter = input("Enter a letter to remove, or type ! if you are done: ")
    if letter == "!":
        break
    strip_letters += letter
    continue

for i in range(len(strip_letters)):
    sentence = sentence.replace(strip_letters[i], "")
print(sentence)
