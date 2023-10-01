def replace_second_word(sentence):
    # replace every second word in a sentence with 'Hello'
    sentence_list = sentence.split(" ")
    for word in range(1, len(sentence_list), 2):
        sentence_list[word] = "Hello"
    return " ".join(sentence_list)


# retrieve user input and run replace second word function
sentence_input = input("Enter a sentence and we'll replace every second word with 'Hello': ")
print(replace_second_word(sentence_input))
