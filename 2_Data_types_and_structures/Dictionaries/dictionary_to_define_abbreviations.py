# set up a dictionary with abbreviations and meanings
abbreviations = {"API": "Application Programming Interface",
                 "IDE": "Integrated Development Environment",
                 "SDK": "Software Development Kit",
                 "UI": "User Interface",
                 "UX": "User Experience",
                 }

# add 2 more abbreviations and meanings to the dictionary
abbreviations.update({"OOP": "Object-Oriented Programming"})
abbreviations.update({"SSH": "Secure Shell"})

# retrieve input abbreviation from user, search dictionary for it, display its meaning, or a statement if not found
user_abbreviation = input("Enter an abbreviation for its meaning: ").upper()
print(abbreviations.get(user_abbreviation, "Abbreviation not found"))
