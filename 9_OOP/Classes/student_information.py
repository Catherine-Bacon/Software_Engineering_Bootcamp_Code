class Student(object):

	def __init__(self, age, name, gender, grades):
		self.age = age
		self.name = name
		self.gender = gender
		self.grades = grades

	def compute_average(self):
		"""Compute the average of the student's grades and print out a message to report the average."""
		average = sum(self.grades)/len(self.grades)
		print("The average for student " + self.name + " is " + str(average))


# Create objects
mike = Student(20, "Mike Edwards", "Male", [64, 65])
sarah = Student(19, "Sarah Jones", "Female", [82, 58])

# Call class functions
Student.compute_average(mike)
