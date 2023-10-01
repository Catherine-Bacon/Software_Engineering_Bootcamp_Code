# retrieve product names from the user
product1 = input("Enter a product name: ")
product2 = input("Enter another product name: ")
product3 = input("Enter another product name: ")

# retrieve the prices of each product
product1price = float(input(f"How much did the {product1} cost (£) to 2 decimal places? "))
product2price = float(input(f"What much did the {product2} cost (£) to 2 decimal places? "))
product3price = float(input(f"What much did the {product3} cost (£) to 2 decimal places? "))

# calculate the total of all three products and the average price
total = float(product1price + product2price + product3price)
average = total / 3

# display results to user to 2 decimal places
print(f'''The total of {product1}, {product2}, {product3} is £{total:.2f} and the average price of the items is £{average:.2f}''')

