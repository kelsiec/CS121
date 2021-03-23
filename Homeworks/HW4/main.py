# TODO 0: Import the functions from coffee.py into your main so that the errors go away in this file. 
# DO NOT move the functions over into main.py. You should use imports so that the functions can stay in coffee.py

# Save the randomly generated number of drinks into the total_drinks variable
total_drinks = get_num_drinks()

# Save the randomly generated drink price into the total_drinks variable
cost_per_drink = get_drink_price()

# The purchase amount before discounts is the number of drinks * their price
overall_price = total_drinks * cost_per_drink

# Use purchase amount to calculate sale discount, save into variable
purchase_discount = bulk_discount(total_drinks,  cost_per_drink)

# Pass the purchase amount and the discount to the print_summary function
print_receipt(overall_price, purchase_discount)
