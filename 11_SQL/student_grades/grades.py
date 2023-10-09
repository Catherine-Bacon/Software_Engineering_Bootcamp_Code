# Import required modules
import sqlite3
from tabulate import tabulate

# Create database and cursor objects
db = sqlite3.connect("grades_db")
cursor = db.cursor()

# Create the table seen in the folder as grades_table.PNG
cursor.execute("""
    CREATE TABLE grades(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
    """)
db.commit()

# Add data to the table
students_grades = [(55, "Carl Davis", 61), (66, "Dennis Fredrickson", 88), (77, "Jane Richards", 78),
                   (12, "Peyton Sawyer", 45), (2, "Lucas Brooke", 99)]
cursor.executemany("""INSERT INTO grades(id, name, grade) VALUES(?,?,?)""",
                   students_grades)
db.commit()

# Print original table
print("\nOriginal table:")
cursor.execute("""SELECT * FROM grades""")
print(tabulate(cursor, headers=["id", "name", "grade"]))

# Select and print all records with a grade between 60 and 80
cursor.execute("""SELECT * FROM grades
 WHERE grade BETWEEN 60 AND 80""")
print("\nAll records with a grade between 60 and 80:")
print(tabulate(cursor, headers=["id", "name", "grade"]))

# Change Carl Davis' grade to 65
grade = 65
name = "Carl Davis"
cursor.execute("""UPDATE grades SET grade = ? WHERE name = ? """, (grade, name))
db.commit()

# Delete Dennis Fredrickson row
name = "Dennis Fredrickson"
cursor.execute("""DELETE FROM grades WHERE name = ? """, (name,))
db.commit()

# Change the grade of all people with an id below than 55
grade = 0
customer_id = 55
cursor.execute("""UPDATE grades SET grade = ? WHERE id < ?""", (grade, customer_id))
db.commit()

# Print final table
print("\nFinal database:")
cursor.execute("""SELECT * FROM grades""")
print(tabulate(cursor, headers=["id", "name", "grade"]))

# Close database
db.close()
