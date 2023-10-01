# set up list of menu items and initialise stock worth variable
menu = ["pasta", "burger", "burrito", "pizza"]
total_stock_worth = 0

# set up dictionaries of menu items and their stock and price
stock = {"pasta": 1,
         "burger": 4,
         "burrito": 8,
         "pizza": 3
         }
price = {"pasta": 6.99,
         "burger": 5.00,
         "burrito": 8.99,
         "pizza": 7.50
         }

# for each item in menu, multiply the item's stock by its price and add to stock worth variable; print result
for item in menu:
    total_stock_worth += stock[item] * price[item]
print(f"The total value of the cafe's stock is £{total_stock_worth}")
