# import module
import random

# create dictionary of jokes
bad_jokes = {"I invented a new word": "Plagiarism",
             "What does a nosy pepper do": "Gets jalapeño business",
             "What do you call a fake noodle?": "An impasta",
             "What type of dog is magic?": "A labracadabrador",
             "What do you get from a pampered cow?": "Spoiled milk"
             }

# select random joke from dictionary, and output answer once the user presses enter
random_joke = random.choice(list(bad_jokes))
print(random_joke)
answer = input("(Press enter for the answer) ")
if answer == "":
    print(bad_jokes[random_joke])
