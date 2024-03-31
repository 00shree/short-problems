menu = {"chocolate cake","vanilla cake","strawberry cake","coffee","latte","capuccino"}
price = {"2.00","3.00","4.00","1.00","2.00","5.00"}
yes_list = {"yes","Yes","y"}


print(menu,price)
while (True):
    order = input("Would you like food or a drink? ")


    if (order == "food"):
        food = ("Enter the food item you'd like to order: ")
        final_order = food

    elif (order == "drink"):
        drink = ("Enter the drink you'd like to order: ")
        final_order = food
        
    if (final_order in menu):
        print("You have ordered a",order)
        clarification = input("is that correct?")

        if (clarification in yes_list):
            for x in menu:
                for y in price:
                        print("The price of your order is",price)
                        break

    else:
        print("Sorry, that is not a valid item.")
            
        
