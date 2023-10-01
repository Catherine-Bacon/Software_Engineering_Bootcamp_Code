# retrieve input from user
word = input("Enter a word: ")

# determine if input string is the same as the reversed string, and print relevant message
if word == word[::-1]:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")
