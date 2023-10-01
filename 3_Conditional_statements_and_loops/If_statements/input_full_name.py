# retrieve input from user (full name)
full_name = input("Enter your full name: ")

'''form conditional statements based on length of input; only between 4 
and 25 characters is valid '''
if len(full_name) == 0:
    print("You haven't entered anything.")
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure you have entered your name and surname.")
elif len(full_name) > 25:
    print("Please make sure that you have only entered your full name.")
elif len(full_name) >= 4 and len(full_name) <= 25:
    print("Thank you for entering your name.")
