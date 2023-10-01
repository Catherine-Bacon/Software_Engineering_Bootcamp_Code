# create email class
class Email:

    # initialise email object and set instance-level variables
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    # output readable email information
    def __str__(self):
        output = f"From: {self.from_address}\nSubject line: {self.subject_line}\n{self.email_contents}\n" \
                 f"Read? {self.has_been_read}\nSpam? {self.is_spam}"
        return output

    # mark email as read
    def mark_as_read(self):
        self.has_been_read = True

    # mark email as spam
    def mark_as_spam(self):
        self.is_spam = True


# create inbox class
class Inbox:

    # initialise inbox object and create empty list to store emails
    def __init__(self):
        self.emails = []

    # creates an email and adds it to inbox
    def add_email(self, from_address, subject_line, email_contents):
        new_email = Email(from_address, subject_line, email_contents)
        self.emails.append(new_email)

    # returns string of indexed subject lines of emails from a sender
    def emails_from_sender_string(self, from_address):
        emails_from_sender = ""
        count = 0
        for email in range(len(self.emails)):
            if self.emails[email].from_address == from_address:
                emails_from_sender += f"{count} {self.emails[email].subject_line}\n"
                count += 1
        if emails_from_sender == "":
            emails_from_sender = "There are no emails in the inbox from this sender."
        return emails_from_sender

    # returns list of emails from a sender
    def emails_from_sender_list(self, from_address):
        emails_from_sender = []
        for email in range(len(self.emails)):
            if self.emails[email].from_address == from_address:
                emails_from_sender.append(self.emails[email])
        return emails_from_sender

    # returns email from a specified user at a specified index and mark it as read
    def get_email(self, from_address, index):
        emails_from_sender = self.emails_from_sender_list(from_address)
        emails_from_sender[index].mark_as_read()
        return emails_from_sender[index]

    # marks the email from a specified user at a specified index as spam
    def mark_as_spam(self, from_address, index):
        sender_address_emails = self.emails_from_sender_list(from_address)
        sender_address_emails[index].mark_as_spam()

    # returns a string of the subject lines of all unread emails
    def get_unread_emails(self):
        unread_emails = "\n"
        for email in range(len(self.emails)):
            if self.emails[email].has_been_read is False:
                unread_emails += self.emails[email].subject_line + ", "
        if unread_emails == "\n":
            unread_emails = "\nThere are no unread emails in the inbox."
        return unread_emails

    # returns a string of the subject lines of all spam emails
    def get_spam_emails(self):
        spam_emails = "\nThe following are subject lines of spam emails:\n"
        for email in range(len(self.emails)):
            if self.emails[email].is_spam is True:
                spam_emails += self.emails[email].subject_line + "\n"
        if spam_emails == "\nThe following are subject lines of spam emails:\n":
            spam_emails = "\nThere are no spam emails in the inbox."
        return spam_emails

    # deletes an email from a specified user at a specified index
    def delete(self, from_address, index):
        emails_from_sender = self.emails_from_sender_list(from_address)
        email_to_delete_subject_line = emails_from_sender[index].subject_line
        for i in range(len(self.emails)):
            if self.emails[i].subject_line == email_to_delete_subject_line and \
                    self.emails[i].from_address == from_address:
                del self.emails[i]


# function to retrieve input index without causing errors
def retrieve_index(input_list):
    while True:
        try:
            index = int(input("Please enter the index of the email you want to select: "))
        except ValueError:
            print("That wasn't a number!")
            continue
        if index < 0 or index >= len(input_list):
            print("This index is out of range.")
            continue
        return index


# initialise inbox for emails
our_inbox = Inbox()

# display menu (program can return to)
while True:
    # retrieve user input
    user_choice = input('''
Welcome to the email system! What would you like to do?

s - send email
l - list emails from a sender
r - read email
m - mark email as spam
gu - get unread emails
gs - get spam emails
d - delete email
e - exit this program
: ''').strip().lower()

    # Send an email (create a new Email object)
    if user_choice == "s":
        # retrieve user inputs
        from_address_input = input("\nPlease enter the address of the sender: ")
        subject_line_input = input("Please enter the subject line of the email: ")
        email_contents_input = input("Please enter the contents of the email: ")
        # add the email to the inbox and print notifying message to user
        our_inbox.add_email(from_address_input, subject_line_input, email_contents_input)
        print("\nEmail has been added to inbox")

    # List all emails from a sender address
    elif user_choice == "l":
        # retrieve user input and list emails from this sender
        from_address_input = input("\nPlease enter the address of the sender: ")
        print(our_inbox.emails_from_sender_string(from_address_input))

    # Read an email
    elif user_choice == "r":
        # retrieve sender address and show emails from the sender with indexes
        from_address_input = input("\nPlease enter the address of the sender of the email: ")
        emails_from_sender_output = our_inbox.emails_from_sender_string(from_address_input)
        print(emails_from_sender_output)
        # retrieve index and display respective email if there are emails from this sender
        if emails_from_sender_output == "There are no emails in the inbox from this sender.":
            continue
        else:
            index_input = retrieve_index(our_inbox.emails_from_sender_list(from_address_input))
            print(our_inbox.get_email(from_address_input, index_input))

    # Mark an email as spam
    elif user_choice == "m":
        # retrieve sender address input and show emails from the sender with indexes
        from_address_input = input("\nPlease enter the address of the sender of the email: ")
        emails_from_sender_output = our_inbox.emails_from_sender_string(from_address_input)
        print(emails_from_sender_output)
        # retrieve email index, mark it as spam and notify user, if there are emails from this sender
        if emails_from_sender_output == "There are no emails in the inbox from this sender.":
            continue
        else:
            index_input = retrieve_index(our_inbox.emails_from_sender_list(from_address_input))
            our_inbox.mark_as_spam(from_address_input, index_input)
        print("\nEmail has been marked as spam")

    # List all unread emails
    elif user_choice == "gu":
        print(our_inbox.get_unread_emails())

    # List all spam emails
    elif user_choice == "gs":
        print(our_inbox.get_spam_emails())

    # Delete an email
    elif user_choice == "d":
        # display indexed emails from inputted sender address
        from_address_input = input("\nPlease enter the address of the sender of the email: ")
        emails_from_sender_output = our_inbox.emails_from_sender_string(from_address_input)
        print(emails_from_sender_output)
        # delete email from inputted index and print success message, if there are emails from the sender
        if emails_from_sender_output == "There are no emails in the inbox from this sender.":
            continue
        else:
            index_input = retrieve_index(our_inbox.emails_from_sender_list(from_address_input))
            our_inbox.delete(from_address_input, index_input)
            print("\nEmail has been deleted")

    # exit the program
    elif user_choice == "e":
        print("\nGoodbye")
        break

    # account for incorrect inputs
    else:
        print("\nOops - incorrect input")
