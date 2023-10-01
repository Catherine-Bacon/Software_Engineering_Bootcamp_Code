# initialise names list
friends_names = ["Fred W", "Giulia P", "Gabby C"]

# print first and last names, and length of list
print(friends_names[0])
print(friends_names[2])
print(len(friends_names))

# initialise ages list
friends_ages = [22, 23, 24]

# (extra) create loop to connect lists
for i in range(len(friends_names)):
    print(f"{friends_names[i]} is {friends_ages[i]} years old")
