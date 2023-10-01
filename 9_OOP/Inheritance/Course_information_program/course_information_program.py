# create course superclass
class Course:
    # establish Course class variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office = "Cape Town"

    # method to print contact details
    def contact_details(self):
        print(f"Please contact us by visiting: {self.contact_website}")

    # method to print head office location
    def head_office_location(self):
        print(f"Head office location: {self.head_office}")


# create OOP Course subclass (Course being superclass)
class OOPCourse(Course):
    # constructor to initialise subclass object (with attributes with pre-assigned values)
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.course_id = "#12345"

    # method to print course description and trainer details
    def trainer_details(self):
        print(f"Course description: {self.description}\nTrainer name: {self.trainer}")

    # method to print course ID info
    def show_course_id(self):
        print(f"ID number: {self.course_id}")


# create subclass object and call methods from subclass and superclass
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
