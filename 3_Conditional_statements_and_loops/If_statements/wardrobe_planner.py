while True:
    # declare variables as booleans and define variables for True case
    temp = True
    weekend = True
    sunny = True

    # establish error check variable
    error = 0

    # retrieve information from the user
    print("Please answer 'Yes' or 'No'")
    temp_check = input("Is the temperature greater than 20 degrees? ").lower()
    weekend_check = input("Is it the weekend? ").lower()
    sunny_check = input("Is is sunny outside? ").lower()

    '''change boolean value according to user input (if required) and increase error
       if there is incorrect input '''
    if temp_check == "no":
        temp = False
        top = "long-sleeved shirt"
    elif temp_check == "yes":
        top = "short-sleeved shirt"
    else:
        error += 1

    if weekend_check == "no":
        temp = False
        bottoms = "jeans"
    elif weekend_check == "yes":
        bottoms = "shorts"
    else:
        error += 1

    if sunny_check == "no":
        temp = False
        accessory = "raincoat"
    elif sunny_check == "yes":
        accessory = "cap"
    else:
        error += 1

    # notify user of incorrect inputs, and output clothes choice if the inputs were correct
    if error > 0:
        print("You have entered a non-Yes/No answer, please try again")
        continue
    else:
        print(f"You should wear a {top} on top, {bottoms} on bottom, with a {accessory}")
        break
