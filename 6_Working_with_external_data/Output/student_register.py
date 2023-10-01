# retrieve input from user
num_students = int(input("How many students are registering? "))

# create new txt file to write to
with open('reg_form', 'w') as f:

    # for the amount of students inputted, ask each for the id number and write this to file
    print("For each student registering")
    for i in range(num_students):
        id_num = input("Enter a student ID number:  ")
        f.write(id_num + "\n")
