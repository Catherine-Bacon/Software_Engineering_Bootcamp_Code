# write a program with two compilation errors, a runtime error and a logical error.
# next to each error, add a comment that explains what type of error it is and why it occurs

# program to find even numbers
num = int(input("Enter a number: "))

if num % 2 == 1: # logical error - should be num % 2 == 0 for even numbers
    print("This number is even!")
elif num % 0 == 0: # runtime error - dividing by 0
    Print("Oops!") # compilaton error - incorrect capitalisation of print()
else:
    print(this number is not even!) # compilation error - missing ""