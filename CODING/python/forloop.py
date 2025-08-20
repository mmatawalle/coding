def calc_price(Name_of_item, Price_of_item):
    print(2)



item_order = 1
# no need 4 this item_order_words = ""


items_and_prices = {}

continue_adding_items = True  
while continue_adding_items:
    if item_order == 1:
        item_order_words = "First item"
    elif item_order == 2:
        item_order_words = "Second item"
    elif item_order == 3:
        item_order_words = "Third item"
    elif item_order == 4:
        item_order_words = "Fourth item"
    elif item_order == 5:
        item_order_words = "Fifth item"
    else:
       item_order_words = f"Item No:{item_order}"

   
    name = input(f"Input the name of the {item_order_words}  you want to add: ").upper()
    price = int(input(f"Input the price of {item_order_words}: $"))
    items_and_prices[name] = price
    item_order += 1
    
    
    if item_order == 1:
        item_order_words = "First item"
    elif item_order == 2:
        item_order_words = "Second item"
    elif item_order == 3:
        item_order_words = "Third item"
    elif item_order == 4:
        item_order_words = "Fourth item"
    elif item_order == 5:
        item_order_words = "Fifth item"
    else:
       item_order_words = f"Item No:{item_order}"
       
       
    while True:
        should_continue = input("Do you want to add another item? 'YES' or 'NO': ").lower()
        if should_continue == "yes":
            break  # exit the mini loop and continue the main loop
        elif should_continue == "no":
            continue_adding_items = False
            break  # exit the mini loop
        else:
            print("Sorry, I didn't understand that. Please type 'YES' or 'NO'.")
print(items_and_prices)
            
    
    
    








#price = int(input("""WELCOME TO SHOPPING CART CALCULATOR  
#                   INPUT THE PRICES YOU WANT TO CALCULATE: \n """))
#total = 0
#for price in prices:
#    total = total + price
#print(f"Total: {total}")





 # confuse d code // item_order_words = str(item_order)