# Import required modules
import sqlite3
from tabulate import tabulate

# Create database and cursor objects
db = sqlite3.connect("students_db")
cursor = db.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE Students(STU_NUM CHAR(6) PRIMARY KEY, S_NAME VARCHAR(15), F_NAME VARCHAR(15),
     INITIAL CHAR(1), START_DATE DATE, COURSE_CODE CHAR(3), PROJ_NUM INT(2))
    """)
db.commit()

# Add data to the table
student_data = [(1, "Snow", "Jon", "E", "05-Apr-14", 201, 6),
                (2, "Stark", "Arya", "C", "12-Jul-17", 305, 11),
                (3, "Lannister", "Jamie", "C", "05-Sep-12", 101, 2),
                (4, "Lannister", "Cercei", "J", "05-Sep-12", 101, 2),
                (5, "Greyjoy", "Theon", "I", "9-Dec-15", 402, 14),
                (6, "Tyrell", "Margaery", "Y", "12-Jul-17", 305, 10),
                (7, "Baratheon", "Tommen", "R", "13-Jun-19", 201, 5)]
cursor.executemany("""INSERT INTO Students(STU_NUM, S_NAME, F_NAME, INITIAL, 
START_DATE, COURSE_CODE, PROJ_NUM) VALUES(?,?,?,?,?,?,?)""", student_data)
db.commit()

# Print table
print("\nOriginal table:")
cursor.execute("""SELECT * FROM Students""")
print(tabulate(cursor, headers=["Student Num", "First Name", "Second Name", "Initial",
                                "Start Date", "Course Code", "Project Num"]))

# List all attributes for a COURSE_CODE of 305
course_code = 305
cursor.execute("""SELECT * FROM Students WHERE COURSE_CODE = ?""", (course_code,))
print("\nStudents with course code 305:")
print(tabulate(cursor.fetchall(), headers=["Student Num", "First Name", "Second Name", "Initial",
                                           "Start Date", "Course Code", "Project Num"]))

# Change the course code to 304 for the person whose student number is 7
course_code = 304
student_num = 7
cursor.execute("""UPDATE Students SET COURSE_CODE = ? WHERE STU_NUM = ?""", (course_code, student_num))
db.commit()

# Delete Jamie Lannister's row, who started on 5 September 2012, whose course code is 101
# and project number is 2 using logical operators
f_name = "Jamie"
s_name = "Lannister"
start_date = "05-Sep-12"
course_code = 101
project_num = 2
cursor.execute("""DELETE FROM Students WHERE F_NAME = ? AND S_NAME = ? AND START_DATE = ? AND
COURSE_CODE = ? AND PROJ_NUM = ?""", (f_name, s_name, start_date, course_code, project_num))
db.commit()

# Change the PROJ_NUM to 14 for students with a course code >= 201, starting before 1 January 2016
grade = 14
course_code = 201
start_date = "1-Jan-2016"
cursor.execute("""UPDATE Students SET PROJ_NUM = ? WHERE COURSE_CODE >= ? AND START_DATE < ?""",
               (grade, course_code, start_date))
db.commit()

# Delete all the data inside a table, but not the table itself
cursor.execute("""DELETE FROM Students""")
db.commit()

# Delete the students table entirely
cursor.execute("""DROP TABLE Students""")
print("\nStudent data table deleted!")
db.commit()

# Close the connection to the database
db.close()
