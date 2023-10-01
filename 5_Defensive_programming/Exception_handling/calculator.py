# create calculator menu to display user options, and for the program to return to
while True:
    # retrieve input from user
    choice = input("\nEnter one of the following options:\n"
                   "C - perform a calculation\n"
                   "V - view all previous calculations from a .txt file\n"
                   ": ").upper()

    # perform a calculation
    if choice == "C":
        # retrieve user operator input and ensure it is a valid operator
        operator = input("\nEnter an operator (+, -, * or /): ")
        while operator not in ["+", "-", "*", "/"]:
            operator = input("This operator is invalid, please re-enter an operator: ")

        # retrieve number inputs, checking for possible divide by zero and value error
        while True:
            try:
                num1 = float(input(f"\nFor your calculation: x {operator} y\nEnter x: "))
                num2 = float(input("Enter y: "))
                if operator == "/" and num2 == 0:
                    print("You cannot divide by zero; please try again.")
                    continue
                break
            except ValueError:
                print("Your inputted a non-number; please try again.")

        # calculate and display resulting calculation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        print(f"\n{num1} {operator} {num2}\n= {result}")

        # output calculation to file of user's choice
        output_file = input("\nEnter the name of the .txt file you want to save this calculation to (without .txt): ")
        with open(f'{output_file}.txt', 'a') as f:
            f.write(f"\n{num1} {operator} {num2} = {result}")

    # view txt file calculations
    elif choice == "V":
        # read to a file of user's choice, asking for txt file name again in case of incorrect input
        while True:
            txt_file = input("\nEnter the name of the .txt file you want to view (without .txt): ")
            try:
                with open(f'{txt_file}.txt', 'r') as f:
                    print(f.read())
                    break
            except FileNotFoundError:
                print(f"{txt_file}.txt does not exist, please retry.")

    # return to menu in case of invalid input
    else:
        print("\nYou inputted an invalid input; please retry")
