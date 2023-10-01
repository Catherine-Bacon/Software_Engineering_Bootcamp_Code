# see error_handling_before for the unedited file
# FIXED CODE WITH COMMENTS

print("Welcome to the error program")# syntax error - missing parentheses
print("\n") # syntax error - missing parentheses and indentation error

ageStr = "24" # indentation error and syntax error - using == instead of =
age = int(ageStr) # indentation error, type error - trying to convert letters to integer - remove 'years old' so it can be an integer
print("I'm " + ageStr + " years old.") # indentation error, syntax - change age to ageStr so can concatenate, and correct spacing
three = 3 # indentation error, type error - remove "" so it is an integer, also this step is unnecessary

answerYears = age + three # indentation error, type error - cannot concatenate string with integer

print(f"The total number of years: {answerYears}") # syntax error - missing parentheses, and "" around variable treating it as string
answerMonths = (answerYears * 12) + 6 # name error - answer does not exist, should be answerYears, logical error - need to include 6 months (+ 6)
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") # syntax error, no brackets used with print statement, type error - need to change answerMonths to string


# FIXED AND CLEANED UP CODE

print("\n\nWelcome to the error program \n")

age = 24
print(f"I'm {age} years old.")

answerYears = age + 3
print(f"The total number of years: {answerYears}")

answerMonths = (answerYears * 12) + 6
print(f"In 3 years and 6 months, I'll be {answerMonths} months old")
