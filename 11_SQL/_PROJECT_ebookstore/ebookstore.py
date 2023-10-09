# IMPORT MODULES
import sqlite3
from tabulate import tabulate
from os.path import exists


# DEFINE FUNCTIONS
def create_table():
    """Create the table and populate it with book data."""
    # Create the table
    cursor.execute("""
        CREATE TABLE e_bookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
        """)
    db.commit()

    # Add data to the table
    books = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
             (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
             (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
             (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
             (3005, "Alice in Wonderland", "Lewis Carroll", 12)]
    cursor.executemany("""INSERT INTO e_bookstore(id, title, author, qty) VALUES(?,?,?,?)""",
                       books)
    db.commit()


def enter_book():
    """Enter a new book into the database, ensuring correct datatypes are added."""
    # Retrieve book data from user
    print("\nEnter the details of the new book:")
    while True:
        while True:
            try:
                book_id = int(input("\nID: "))
            except ValueError:
                print("The book ID must be an integer.")
                continue
            if cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,)):
                if cursor.fetchone() is not None:
                    print("Please enter a unique ID.")
                    continue
                else:
                    break
        title = input("Title: ")
        author = input("Author: ")
        while True:
            try:
                qty = int(input("Qty: "))
            except ValueError:
                print("The quantity must be an integer.")
                continue
            else:
                break

        # Ensure data is correct before committing
        print("\n")
        print(tabulate([["ID", "Title", "Author", "Qty"],
                        [book_id, title, author, qty]],
                       headers='firstrow'))
        check = input("\nAre you sure you want to add the above book to your directory? (y/n): ").lower()
        if check == "y":
            cursor.execute("""INSERT INTO e_bookstore(id, title, author, qty) VALUES(?,?,?,?)""",
                           (book_id, title, author, qty))
            print("\n\tNew book inserted!")
            db.commit()
            return
        else:
            # Offer user to retry or exit to menu
            option = input("Enter r for retry or e for exit to the menu (r/e): ").lower()
            if option == "r":
                enter_book()
            else:
                return


def update_book():
    """Update book info in the database, ensuring correct datatypes are added."""
    # Get the book ID
    while True:
        try:
            book_id = int(input("\nEnter the ID of the book you would like to update: "))
        except ValueError:
            print("The book ID must be an integer.")
            continue
        break

    # Check ID in directory
    cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
    checker = cursor.fetchone()
    if checker is None:
        print("\nThere is no such book with that ID in the directory.")
        option = input("Enter r for retry or e for exit to the menu (r/e): ").lower()
        if option == "r":
            update_book()
        else:
            return

    # Get column to change
    print("\n")
    cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
    print(tabulate(cursor, headers=["ID", "Title", "Author", "Qty"]))
    print("\n")
    while True:
        try:
            change_data = int(input("Enter the column you would like to change (1/2/3/4) : ").lower())
        except ValueError:
            print("The book ID must be an integer.")
            continue
        if change_data not in [1, 2, 3, 4]:
            continue
        else:
            # Get the new value for the column
            new_value = input("Enter the new value: ")
            if change_data == 1:
                try:
                    int(new_value)
                except ValueError:
                    print("The book ID must be an integer.")
                    continue
                cursor.execute("""UPDATE e_bookstore SET id = ? WHERE id = ?""",
                               (new_value, book_id))
            elif change_data == 2:
                cursor.execute("""UPDATE e_bookstore SET title = ? WHERE id = ?""",
                               (new_value, book_id))
            elif change_data == 3:
                cursor.execute("""UPDATE e_bookstore SET author = ? WHERE id = ?""",
                               (new_value, book_id))
            else:
                while True:
                    try:
                        int(new_value)
                    except ValueError:
                        print("The book ID must be an integer.")
                        new_value = input("Enter the new value: ")
                        continue
                    break
                cursor.execute("""UPDATE e_bookstore SET qty = ? WHERE id = ?""",
                               (new_value, book_id))
            print("\n")

            # Ensure new information is correct
            cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
            print(tabulate(cursor, headers=["ID", "Title", "Author", "Qty"]))
            while True:
                option = input("Is this new information correct (y/n)? ").lower()
                if option == "y":
                    db.commit()
                    print("\n\tBook updated!")
                    return
                if option == "n":
                    db.rollback()
                    option = input("Enter r for retry or e for exit to the menu (r/e): ").lower()
                    if option == "r":
                        update_book()
                    else:
                        return
                else:
                    "Please enter either y or n."


def delete_book():
    """Delete book in the database."""
    # Get ID of the book to delete
    print_table()
    book_id = input("\nEnter the ID of the book you want to delete: ")
    cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
    print(tabulate(cursor, headers=["ID", "Title", "Author", "Qty"]))
    option = input("\nIs this the book you want to delete (y/n): ").lower()
    if option == "y":
        # Delete the book
        cursor.execute("""DELETE FROM e_bookstore WHERE id = ?""", (book_id,))
        print("\n\tBook deleted!")
        db.commit()
    else:
        # Offer user to retry or exit
        option = input("Enter r for retry or e for exit to the menu (r/e): ").lower()
        if option == "r":
            delete_book()
        else:
            return


def search_for_book():
    """Search for a new book in the database to receive all its data."""
    # Get the books ID
    while True:
        try:
            book_id = int(input("\nEnter the book's ID: "))
        except ValueError:
            print("The book ID must be an integer.")
            continue
        break

    cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
    if cursor.fetchone() is None:
        print("There is no book with that ID in the directory.")
        # Offer user to retry or exit to menu
        option = input("Enter r for retry or e for exit to the menu (r/e): ").lower()
        if option == "r":
            search_for_book()
        else:
            return

    # Print the searched book's info
    cursor.execute("""SELECT * FROM e_bookstore WHERE id = ?""", (book_id,))
    print(tabulate(cursor, headers=["ID", "Title", "Author", "Qty"]))
    print("\n")


def print_table():
    """Print the table in a readable format."""
    cursor.execute("""SELECT * FROM e_bookstore""")
    print("\n")
    print(tabulate(cursor, headers=["ID", "Title", "Author", "Qty"]))


# MAIN
# Check if database is new
if exists("bookstore_db"):
    new_database = True
else:
    new_database = False

# Connect to database and create cursor object
db = sqlite3.connect("bookstore_db")
cursor = db.cursor()

# if database does not exist, create it
if not new_database:
    create_table()

while True:
    # Print menu
    choice = int(input("\n1. Enter new book"
                       "\n2. Update book info"
                       "\n3. Delete book"
                       "\n4. Search for book"
                       "\n5. Print directory"
                       "\n0. Exit"
                       "\n\nChoose from 0-5: "))
    if choice == 1:
        # Enter a new book
        enter_book()
    elif choice == 2:
        # Update book
        update_book()
    elif choice == 3:
        # Delete book
        delete_book()
    elif choice == 4:
        # Search for book
        search_for_book()
    elif choice == 5:
        # Print the table
        print_table()
    elif choice == 0:
        # Exit
        print("\nGoodbye!")
        db.close()
        break
    else:
        print("\nChoice not recognised, please retry")
