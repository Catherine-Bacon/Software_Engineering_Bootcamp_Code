# le - length, wi - width, he - height, ra - radius
def square(le):
    return le * le


def rectangle(wi, he):
    return wi * he


def circle(ra):
    return 3.14 * ra ** 2


def options():
    print("\nOptions:\n"
          "s = calculate the area of a square.\n"
          "c = calculate the area of a circle.\n"
          "r = calculate the area of a rectangle.\n"
          "q = quit.")


print("This program will calculate the area of a square, circle or rectangle.")
choice = "x"
options()
while choice != "q":
    choice = input("\nPlease enter your choice: ")
    if choice == "s":
        length = float(input("Length of square: "))
        print("\nThe area of this square is", square(length))
        options()
    elif choice == "c":
        radius = float(input("Radius of the circle: "))
        print("\nThe area of the circle is", circle(radius))
        options()
    elif choice == "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("\nThe area of the rectangle is", rectangle(width, height))
        options()
    elif choice == "q":
        print("",)
    else:
        print("\nUnrecognized option.")
        options()
