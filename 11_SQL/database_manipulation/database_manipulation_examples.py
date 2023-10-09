# Import modules and create database and cursor objects
import sqlite3
db = sqlite3.connect("student_table_db")
cursor = db.cursor()  # Get a cursor object

# Create table
cursor.execute("""
    CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
""")
db.commit()

name1 = "Andres"
grade1 = 60
name2 = "John"
grade2 = 90

# Insert students
cursor.execute("""INSERT INTO student(name, grade)
                  VALUES(?,?)""", (name1, grade1))
print("First user inserted")
cursor.execute("""INSERT INTO student(name, grade)
                  VALUES(?,?)""", (name2, grade2))
print("Second user inserted")
db.commit()

# Display student data
print("\nBelow is the data:")
with db:
    cursor.execute("SELECT * FROM student")
    print(cursor.fetchall())

# Print last id
customer_id = cursor.lastrowid
print("\nLast row id: %d" % customer_id)

# Print data of student with id 1
customer_id = 1
cursor.execute("""SELECT name, grade FROM student WHERE id=?""", (customer_id,))
student = cursor.fetchone()
print("Data retrieved about student with id %d:" % customer_id)
print(student)

# Update user with id 1
grade = 100
customer_id = 1
cursor.execute("""UPDATE student SET grade = ? WHERE id = ? """, (grade, customer_id))
print("\nStudent data updated!\n")

# Display all student's name and grade
print("SELECT name, grade FROM student:")
cursor.execute("""SELECT name, grade FROM student""")
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print("{0} : {1}".format(row[0], row[1]))

# Delete user with id 2
customer_id = 2
cursor.execute("""DELETE FROM student WHERE id = ? """, (customer_id,))
print("\nStudent %d deleted" % customer_id)

# Delete the table
cursor.execute("""DROP TABLE student""")
print("student table deleted!")
db.commit()

db.close()
print("Connection to database closed")
