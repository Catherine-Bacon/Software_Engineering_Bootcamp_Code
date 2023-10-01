# setup output formatting
bold = '\033[1m'
reset = '\033[0m'

# read data from file
with open('DOB.txt', 'r+') as f:

    # iterate through lines to retrieve and print first two words
    print(f"{bold}Name{reset}")
    for line in f:
        words = line.split()
        name = words[:2]
        print(" ".join(name))

    # go to start of file
    f.seek(0)

    # iterate through lines to retrieve and print last three words
    print(f"\n{bold}Birthdate{reset}")
    for line in f:
        words = line.split()
        dob = words[2:]
        print(" ".join(dob))
