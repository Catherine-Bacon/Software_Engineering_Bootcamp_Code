def print_numbers(numbers):
    print("\nTelephone Numbers:")
    for x in numbers.keys():
        print("Name:", x, "\tNumber:", numbers[x])


def add_number(numbers, first_name, number):
    numbers[first_name] = number


def lookup_number(numbers, first_name):
    if first_name in numbers:
        return "The number is " + numbers[first_name]
    else:
        return first_name + " was not found"


def remove_number(numbers, first_name):
    if first_name in numbers:
        del numbers[first_name]
    else:
        print(first_name, " was not found")


def load_numbers(numbers, file):
    in_file = open(file, "r")
    for in_line in in_file:
        in_line = in_line.rstrip('\n')     
        first_name, number = in_line.split(",")
        numbers[first_name] = number
    in_file.close()

    return numbers


def save_numbers(numbers, file):
    number_list = open(file, "w")
    for x in numbers.keys():
        number_list.write(x + "," + numbers[x] + "\n")
    number_list.close()


def print_menu():
    print('\n1. Print Phone Numbers'
          '\n2. Add a Phone Number'
          '\n3. Remove a Phone Number'
          '\n4. Lookup a Phone Number'
          '\n5. SAVE CHANGES'
          '\n6. Quit')


phone_list = {}
menu_choice = 0
print_menu()
file_name = "TelNums.txt"
phone_list = load_numbers(phone_list, file_name)

while True:
    menu_choice = int(input("\nType in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("\nAdd Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("\nRemove Name and Number")
        name = input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("\nLookup Number")
        name = input("Name: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        # filename = input("\nFilename to save: ")
        save_numbers(phone_list, file_name)
    elif menu_choice == 6:
        break
    else:
        print_menu()

print("\nGoodbye")
