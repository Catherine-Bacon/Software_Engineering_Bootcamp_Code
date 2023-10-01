# create adult superclass
class Adult:
    # initialise Adult class object
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # method to print the person can drive
    def can_drive(self):
        print(f"{self.name} is {self.age} and therefore is old enough to drive")


class Child(Adult):
    # initialise the Child subclass, so it has the same attributes as the Adult class
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    # method to override superclass can_drive method
    def can_drive(self):
        print(f"{self.name} is {self.age} and therefore is too young to drive")


# retrieve user inputs and ensure age input is an integer
name_input = input("Enter the person's name: ")
while True:
    try:
        age_input = int(input("Enter the person's age: "))
        break
    except ValueError:
        print("That wasn't a number! Try again.")
eye_colour_input = input("Enter the person's eye colour: ")
hair_colour_input = input("Enter the person's hair colour: ")

# determine whether the new person is a child or adult (from age) and create an object accordingly
if age_input >= 18:
    new_person = Adult(name_input, age_input, eye_colour_input, hair_colour_input)
else:
    new_person = Child(name_input, age_input, eye_colour_input, hair_colour_input)

# call the can_drive method
new_person.can_drive()
