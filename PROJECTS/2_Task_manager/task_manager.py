# read input files, storing data in lists
with open('user.txt', 'r') as f:
    user_details = f.read()
login_list = user_details.split("\n")
with open('tasks.txt', 'r') as f:
    tasks = f.read()
task_list = tasks.split("\n")

# create dictionary to store usernames and passwords
login_dict = {}
for i in range(len(login_list)):
    split_data = login_list[i].split(", ")
    key = split_data[0]
    value = split_data[1]
    login_dict[key] = value

# request user to login and check against login dictionary; allow user in if correct and re-ask for details if not
user_username = input("LOGIN\nEnter your username: ")
user_password = input("Enter your password: ")
while user_username not in login_dict.keys():
    user_username = input("This username is invalid.\nEnter your username: ")
    user_password = input("Enter your password: ")
while user_password != login_dict[user_username]:
    user_password = input("This password is invalid. \nEnter your password: ")
print("You have successfully logged in!")

# present the menu to the user and convert input to lower case; offer different menu if user has the username 'admin'
while True:
    if user_username == "admin":
        menu = input('''\nMENU\nSelect one of the following options:
        r - Register a user
        a - Add a task
        va - View all tasks
        vm - View my tasks
        s - View statistics
        e - Exit
        : ''').lower()
    else:
        menu = input("""\nMENU\nSelect one of the following options:
        r - Register a user
        a - Add a task
        va - View all tasks
        vm - View my tasks
        e - Exit
        : """).lower()

    # registering a user
    if menu == "r":
        # allow user to register users if they have the username 'admin'
        if user_username == "admin":
            # retrieve username and password inputs from user, making sure the username is not already registered
            new_username = input("\nREGISTER A USER\nInput the new user's username: ")
            while new_username in login_dict.keys():
                new_username = input("This username is already registered. \nInput a different username: ")
            new_password = input("Input the new user's password: ")
            password_check = input("Confirm the password: ")
            # ensure password and password-check match, then add user details to user txt file
            while new_password != password_check:
                password_check = input("Passwords do not match; please re-confirm the password: ")
            with open('user.txt', 'a') as f:
                f.write(f"\n{new_username}, {new_password}")
            print("You have registered a new user!")
        # redirect to menu if not the user 'admin'
        else:
            print("\nOnly 'admin' can register users, please try another option from the menu.")

    # adding a task
    elif menu == "a":
        # retrieve task data from user
        username = input("\nADD A TASK\nEnter the username of the person whom the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a description of the task: ")
        set_date = input("Enter the current date: ")
        due_date = input("Enter the due date of the task: ")
        task_status = "No"
        # add new task data to tasks txt file
        with open('tasks.txt', 'a') as f:
            f.write(f"\n{username}, {task_title}, {task_description}, {set_date}, {due_date}, {task_status}")

    # view all tasks
    elif menu == "va":
        # create empty output string and output each line from the file in a readable format
        output = "\nVIEW ALL TASKS\n"
        for i in range(len(task_list)):
            split_data = task_list[i].split(", ")
            output += u'\u2500' * 130
            output += f"\nTask: \t\t\t\t{split_data[1]}\n"
            output += f"Assigned to: \t\t{split_data[0]}\n"
            output += f"Date assigned: \t\t{split_data[3]}\n"
            output += f"Due date: \t\t\t{split_data[4]}\n"
            output += f"Task complete? \t\t{split_data[5]}\n"
            output += f"Description: \t\t{split_data[2]}\n"
            output += u'\u2500' * 130
        print(output)

    # view all tasks of logged on user
    elif menu == "vm":
        # create empty output string, and print task details if username from task is the same as logged on user
        output = "\nVIEW MY TASKS\n"
        for i in range(len(task_list)):
            split_data = task_list[i].split(", ")
            if split_data[0] == user_username:
                output += u'\u2500' * 130
                output += f"\nTask: \t\t\t\t{split_data[1]}\n"
                output += f"Assigned to: \t\t{split_data[0]}\n"
                output += f"Date assigned: \t\t{split_data[3]}\n"
                output += f"Due date: \t\t\t{split_data[4]}\n"
                output += f"Task complete? \t\t{split_data[5]}\n"
                output += f"Description: \t\t{split_data[2]}\n"
                output += u'\u2500' * 130
        print(output)

    # display statistics
    elif menu == "s":
        # print out to the user the number of tasks and number of users to the user 'admin' in a readable format
        if user_username == 'admin':
            num_tasks = len(task_list)
            num_users = len(login_list)
            output = "\nVIEW STATISTICS\n"
            output += u'\u2500' * 50
            output += f"\nTotal number of tasks: \t\t\t\t{num_tasks}\n"
            output += f"Total number of users: \t\t\t\t{num_users}\n"
            output += u'\u2500' * 50
            print(output)
        # redirect to menu if not the user 'admin'
        else:
            print("\nYou have made a wrong choice, please try again")

    # exit menu (end program)
    elif menu == "e":
        print("\nGoodbye!")
        exit()

    # account for incorrect input, restart menu
    else:
        print("\nYou have made a wrong choice, please try again")
