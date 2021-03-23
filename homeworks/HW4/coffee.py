# TODO 0: Import math and random, or just the functions you need from those modules

# get_num_drinks
#    Parameters: none
#    Return: should generate and return the number of drinks to order
#    Side effect: should print the number of drinks
def get_num_drinks():
  num_drinks = 0    # TODO 1: generate a random number between 2 and 12
  print()      # TODO 2: print how many drinks were ordered to the screen, in a full sentence.
  return num_drinks

# get_drink_price
#    Parameters: none
#    Return: should choose and return one of four drink costs
#    Side effect: should print the drink price
def get_drink_price():
    drink_type = 0 # TODO 3: generate a random number representing the drink type

    drink_price = 0
    # TODO 4: write if-statements based on drink_type that will set drink_price to the appropriate value

    print() # TODO 5: print the drink price to the screen, in a full sentence including $ and punctuation.
    return drink_price

# bulk_discount
#    Parameters: none
#    Return: A discount equal to the square root of the 
        # total purchase amount, in decimal form.     
        # e.g. If the customer spend $25, this is a 5% discount, and should be returned as .05.
#    Side effect: if the user buys at least six drinks, AND each drink costs at least $4, print "Wow, you must really like your friends!"
def bulk_discount(total_drinks, price_per_drink):
    amount = 0.0 # TODO 6: calculate the square root of the purchased amount, using the math module. Remember to return the percentage as a decimal, e.g. .05 rather than 5.

    # TODO 7: if the user buys at least six drinks, and each drink costs at least $4, print "Wow, your friends must really like you!"
    return amount

# print_receipt
#    Parameters: amount spent, discount
#    Return: none
#    Side effect: prints a summary of the customer's purchase and discount savings
def print_receipt(original_total, discount):
  human_readable_discount = 0 # TODO 8: Generate the human-readable discount from the discount variable, e.g. .06 should be 6, to print a 6% discount

  saved = original_total * discount
  new_total = original_total - discount

  # TODO 9: Fix the formatting of the summary below to print exactly 2 decimal places for each number
  # TODO 10: Check the output and make sure that it makes sense. If not, it means there are bugs still in the code.
  print("****** CUSTOMER DISCOUNT SUMMARY ******")
  print("---------------------------------------")
  print("Total purchase amount: \t\t  $", original_total, sep="")
  print(human_readable_discount, "% Discount: \t\t\t -$", saved, sep="")
  print("---------------------------------------")
  print("TOTAL AFTER DISCOUNT\t\t  $", new_total, sep="")
  print("---------------------------------------")
  print("You Saved\t\t\t\t\t  $", discount, sep="")
  print("---------------------------------------")