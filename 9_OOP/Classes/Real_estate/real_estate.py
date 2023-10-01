# property listing class
class PropertyListing:

    # initialise propertylisting object and set instance-level variables
    def __init__(self, property_details, property_type, property_agent, for_sale_or_rent):
        self.property_details = property_details
        self.property_type = property_type
        self.property_agent = property_agent
        self.is_available = True
        self.property_viewed = False
        self.for_sale_or_rent = for_sale_or_rent

    # output readable property information
    def __str__(self):
        output = f"Property details: {self.property_details}\nProperty type: {self.property_type}\n Property agent: " \
                 f"{self.property_agent}\nAvailable? {self.is_available}\nViewed? {self.property_viewed}\n" \
                 f"For sale or rent? {self.for_sale_or_rent}\n"
        return output

    # change property viewing status to true (has been viewed)
    def view_property(self):
        self.property_viewed = True


# create listing class
class Listings:

    # initialise listings object and create empty list to store listings
    def __init__(self):
        self.listings = []

    # creates a listing and adds it to the listings list
    def add_property(self, property_details, property_type, property_agent, for_sale_or_rent):
        new_property = PropertyListing(property_details, property_type, property_agent, for_sale_or_rent)
        self.listings.append(new_property)

    # returns the number of listings
    def get_count(self):
        return len(self.listings)

    # sets a property at an index as not being available
    def get_property(self, index):
        self.listings[index].is_available = False
        return self.listings[index]

    # returns the list of properties which are for sale
    def get_properties_for_sale(self):
        properties_for_sale = []
        for listing in range(len(self.listings)):
            if self.listings[listing].for_sale_or_rent == "Sale":
                properties_for_sale.append(self.listings[listing])
        return properties_for_sale

    # returns the list of properties which are for rent
    def get_properties_for_rent(self):
        properties_for_rent = []
        for listing in range(len(self.listings)):
            if self.listings[listing].for_sale == "Rent":
                properties_for_rent.append(self.listings[listing])
        return properties_for_rent

    # deletes properties which are not available
    def delete_property(self):
        for listing in range(len(self.listings)):
            if self.listings[listing].is_available is False:
                del self.listings[listing]


# initialise listings list to store properties
our_listings = Listings()

# display menu (program can return to)
while True:
    # retrieve user input
    user_choice = input('''
Welcome to your properties menu! What would you like to do?

a - add a property
g - get a property (set as not available)
va - view all available properties
vs - view properties for sale
vr - view properties for rent
d - delete all not available properties
e - exit this program
: ''').strip().lower()

    # Add a property
    if user_choice == "a":
        # retrieve user inputs
        property_details_input = input("Enter the property details (Address, City, Zipcode, Size, Bed, Bathroom, \
        Features): ")
        property_type_input = input("Enter the property type (house, linked house, apartment): ")
        property_agent_input = input("Enter the property agent: ")
        while True:
            for_sale_or_rent_input = input("Is this property for sale or rent? (s/r) : ").lower().strip()
            if for_sale_or_rent_input == "s":
                for_sale_or_rent_input = "Sale"
                break
            elif for_sale_or_rent_input == "r":
                for_sale_or_rent_input = "Rent"
                break
            else:
                print("Incorrect input, please retry. ")
                continue
        # add the property to the listings list and print notifying message to user
        our_listings.add_property(property_details_input, property_type_input, property_agent_input,
                                  for_sale_or_rent_input)
        print("The property has been added to your listings.")

    # Get a property (set as not available)
    elif user_choice == "g":
        # display properties and their contents to user and ask for index
        for i in range(len(our_listings.listings)):
            print(f"{i}:\n{our_listings.listings[i]}")
        index_input = int(input("Enter the property index would you like to get (set as not available): "))
        our_listings.get_property(index_input)
        print(f"The property at {index_input} been marked as not available.")

    # View all available properties
    elif user_choice == "va":
        for i in range(len(our_listings.listings)):
            print(our_listings.listings[i])

    # View properties for sale
    elif user_choice == "vs":
        our_properties_for_sale = our_listings.get_properties_for_sale()
        for i in range(len(our_properties_for_sale)):
            print(our_properties_for_sale[i])

    # View properties for rent
    elif user_choice == "vr":
        our_properties_for_rent = our_listings.get_properties_for_rent()
        for i in range(len(our_properties_for_rent)):
            print(our_properties_for_rent[i])

    # deletes properties which aren't available (have been leased or sold)
    elif user_choice == "d":
        # delete not available properties from listings list and display success message to user
        for i in range(len(our_listings.listings)):
            if our_listings.listings[i].is_available is False:
                del our_listings.listings[i]
        print("All leased/sold properties have been deleted")

    # exit the program
    elif user_choice == "e":
        print("Goodbye")
        break

    # account for incorrect inputs
    else:
        print("Oops - incorrect input")
