# IMPORT FUNCTIONS
from datetime import date
from datetime import datetime

# IMPORT DATA
# read input files, storing data in lists
with open('user.txt', 'r') as file:
    user_details = file.read()
login_list = user_details.split("\n")
with open('tasks.txt', 'r') as file:
    tasks = file.read()
task_list = tasks.split("\n")


# DEFINE FUNCTIONS
def reg_user():
    """
    Function for admin to register a user (add login details to user.txt), by prompting the user to input a username
    (checked against the usernames already registered in user.txt to prevent repetition) and password (asked to be
    inputted twice for confirmation)
    """
    # check user is admin
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


def add_task():
    """
    Function to add a task to tasks.txt, by prompting the user for username the task is set to, the task title,
    description, due date, and task status. The assigned date is set as the current date and the task status (whether it
    has been completed) is set to "No"
    """
    # retrieve task data from user
    username = input("\nADD A TASK\nEnter the username of the person whom the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    assigned_date = date.today()
    while True:
        try:
            due_date = datetime(int(input("Input the due date (in numbers)\nEnter the year: ")),
                                int(input("Enter the month: ")),
                                int(input("Enter the day of the month: ")))
            break
        except ValueError:
            print("Your input was incorrect, please retry.")
    task_status = "No"
    # add new task data to tasks txt file
    with open('tasks.txt', 'a') as f:
        f.write(f"\n{username}, {task_title}, {task_description}, {assigned_date}, {due_date}, {task_status}")


def view_all():
    """
    Function to view all tasks and display the information for each in a readable format
    """
    # loop over task list and print information to an output string
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


def view_mine():
    """
    Function to view all tasks which are assigned to the user that is currently logged in, in a readable and numbered
    format. The user is prompted to input an index or return to the main menu. If an index is entered they can edit the
    related task in the following ways: mark it as complete, edit who the task is assigned to or edit the
    due date
    """
    # create output string, counter variable, and variables to track which lines of txt file relate to user
    output = "\nVIEW MY TASKS\n"
    count = 0
    line_num = -1
    user_task_line_nums = []
    # record details of tasks assigned to the logged on user, incrementing/tracking the lines relating to the user
    for i in range(len(task_list)):
        split_data = task_list[i].split(", ")
        line_num += 1
        if split_data[0] == user_username:
            count += 1
            output += u'\u2500' * 130
            output += f"\nTask {count}: \t\t\t{split_data[1]}\n"
            output += f"Assigned to: \t\t{split_data[0]}\n"
            output += f"Date assigned: \t\t{split_data[3]}\n"
            output += f"Due date: \t\t\t{split_data[4]}\n"
            output += f"Task complete? \t\t{split_data[5]}\n"
            output += f"Description: \t\t{split_data[2]}\n"
            output += u'\u2500' * 130
            user_task_line_nums.append(line_num)
    # print notifying message if no tasks have been assigned to the user, otherwise print the task data
    if output == "\nVIEW MY TASKS\n":
        print("There are no tasks assigned to you.")
    else:
        print(output)
        # retrieve index from user and ensure the input is an integer, and the index is within the tasks list range
        while True:
            try:
                index = int(input("Enter the index of the task you would like to select, "
                                  "or enter -1 to return to the main menu: "))
                if index <= -2 or index == 0 or index > count:
                    print("Oops, the index you entered was out of range, please try again.")
                    continue
                break
            except ValueError:
                print("Oops, you didn't enter a number, please try again.")
        # if the user enters -1 return to the main menu (exit function)
        if index == -1:
            return

        # display options to user, ensuring a correct option is inputted
        choice = input("\nWhat would you like to do?\nm - Mark the task as complete"
                       "\neu - Edit who the task is assigned"
                       " to\ned - Edit due date\n: ").lower()
        while choice != "m" and choice != "eu" and choice != "ed":
            choice = input("That choice was invalid, please re-enter: ").lower()
        for i in range(len(task_list)):
            # identify task_list line which relates to user's task they wish to edit
            if i == user_task_line_nums[index - 1]:
                split_data = task_list[i].split(", ")
                # mark the task as complete
                if choice == "m":
                    split_data[5] = "Yes"
                    print("This task has been marked as completed.")
                    break
                # ensure the task is only edited if it is incomplete
                if split_data[5] == "Yes":
                    print("\nSorry, only tasks which are incomplete can be edited.")
                    break
                else:
                    # change who the task is assigned to
                    if choice == "eu":
                        new_assigned_to = input("Enter the username of the person you want to assign the task to: ")
                        split_data[0] = new_assigned_to
                        print("The person the task is assigned to has been changed.")
                        break
                    # input a new due date
                    elif choice == "ed":
                        new_due_date = input("Enter the new due date of the task: ")
                        split_data[4] = new_due_date
                        print("This task has been marked as completed.")
                        break
                task_list[i] = ", ".join(split_data)
        # write new task info to tasks txt file
        with open('tasks.txt', 'w') as f:
            f.write("\n".join(task_list))


def view_statistics():
    """
    Function for admin to view statistics (generated reports from generate_reports function), in a readable format
    """
    # ensure user is 'admin'
    if user_username == 'admin':
        # generate reports with function to ensure up-to-date information is displayed
        generate_reports()
        with open('task_overview.txt', 'r') as f:
            task_overview_info = f.read()
        print(f"\n{task_overview_info}\n")
        with open('user_overview.txt', 'r') as f:
            user_overview_info = f.read()
        print(user_overview_info)
    # redirect to menu if not the user 'admin'
    else:
        print("\nYou have made a wrong choice, please try again")


def generate_reports():
    """
    Function to generate two reports (txt files); task_overview contains general information about the tasks (total
    no., no. complete, incomplete, incomplete and overdue, and percentage overdue, complete, then user_overview contains
    information about each user's tasks (no. assigned to them, percentage of total assigned to them, percentage
    completed, incomplete, and those which are incomplete and overdue)
    """
    # create counter variables and count completed, overdue, and incomplete and overdue tasks
    completed_count = 0
    incomplete_overdue_count = 0
    overdue_count = 0
    for i in range(len(task_list)):
        split_data = task_list[i].split(", ")
        if split_data[5] == "Yes":
            completed_count += 1
        if split_data[5] == "Yes" and datetime.strptime(split_data[4], '%d/%m/%Y').date() <= date.today():
            incomplete_overdue_count += 1
        if datetime.strptime(split_data[4], "%d/%m/%Y").date() <= date.today():
            overdue_count += 1
    # create and add information to task overview variable, and write to txt file
    task_overview = "TASK OVERVIEW\n\n"
    task_overview += f"Total number of tasks that have been generated and tracked: {len(task_list)}\n"
    task_overview += f"Number of completed tasks: {completed_count}\n"
    task_overview += f"Number of uncompleted tasks: {len(task_list) - completed_count}\n"
    task_overview += f"Number of tasks which have not been completed and are overdue: {incomplete_overdue_count}\n"
    task_overview += f"Percentage of tasks that are incomplete: "
    task_overview += f"{100 * (len(task_list) - completed_count) / len(task_list)}\n"
    task_overview += f"Percentage of tasks that are overdue: {100 * overdue_count / len(task_list)}"
    with open('task_overview.txt', 'w') as f:
        f.write(task_overview)

    # create and add information to user overview variable
    user_overview = "USER OVERVIEW\n\n"
    user_overview += f"Number of users registered: {len(login_list)}\n"
    user_overview += f"Total number of tasks that have been generated and tracked: {len(task_list)}\n"
    # for each user, create counter variables and count user tasks, complete, and incomplete and overdue
    for username in range(len(list(login_dict.keys()))):
        user = list(login_dict.keys())[username]
        user_task_count = 0
        user_completed_count = 0
        user_incomplete_overdue_count = 0
        for i in range(len(task_list)):
            split_data = task_list[i].split(", ")
            if split_data[0] == user:
                user_task_count += 1
                if split_data[5] == "Yes":
                    user_completed_count += 1
                if split_data[5] == "No" and datetime.strptime(split_data[4], '%d/%m/%Y').date() <= date.today():
                    user_incomplete_overdue_count += 1
        # add information to user overview variable and write final variable with all user information to txt file
        user_overview += f"\nFOR USERNAME: {user}\n"
        user_overview += f"Number of tasks assigned to user: {user_task_count}\n"
        user_overview += f"Percentage of total number of tasks that have been assigned to user: "
        user_overview += f"{100*user_task_count/len(task_list)}\n"
        user_overview += f"The percentage of tasks assigned to this user that have been completed: "
        user_overview += f"{100*user_completed_count/len(task_list)}\n"
        user_overview += f"The percentage of tasks assigned to this user that must still be completed: "
        user_overview += f"{100 - (100*user_completed_count/len(task_list))}\n"
        user_overview += f"The percentage of tasks assigned to this user have not been completed and are overdue: "
        user_overview += f"{100*user_incomplete_overdue_count/len(task_list)}"
    with open('user_overview.txt', 'w') as f:
        f.write(user_overview)


# LOGIN SECTION
# create dictionary to store usernames and passwords
login_dict = {}
for line in range(len(login_list)):
    split_login_list = login_list[line].split(", ")
    key = split_login_list[0]
    value = split_login_list[1]
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

# MENU SECTION
# present the menu to the user and convert input to lower case; offer different menu if user has the username 'admin'
while True:
    if user_username == "admin":
        menu = input('''\nMENU\nSelect one of the following options:
        r - Register a user
        a - Add a task
        va - View all tasks
        vm - View my tasks
        s - View statistics
        g - Generate reports
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
        reg_user()

    # adding a task
    elif menu == "a":
        add_task()

    # view all tasks
    elif menu == "va":
        view_all()

    # view all tasks of logged on user
    elif menu == "vm":
        view_mine()

    # display statistics
    elif menu == "s":
        view_statistics()

    # generate reports
    elif menu == "g":
        generate_reports()

    # exit menu (end program)
    elif menu == "e":
        print("\nGoodbye!")
        exit()

    # account for incorrect input, restart menu
    else:
        print("\nYou have made a wrong choice, please try again")
