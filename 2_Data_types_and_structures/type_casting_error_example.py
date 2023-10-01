# retrieve inputs from the user
fav_rest = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))

# print out the inputs using separate print() statements
print(fav_rest)
print(int_fav)

# cast fav_rest to be an integer
print(int(fav_rest))
''' this outputs an error as the string has to be made
up of numerical characters to be converted - int(string) only works with a 
string representation of an integer, e.g. int("7") '''