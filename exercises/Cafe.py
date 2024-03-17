menu = {"chocolate cake","vanilla cake","strawberry cake"}
price = {"2.00","3.00","4.00"}
yes_list = {"yes","Yes","y"}

while (True):
    order = input("What would you like to order? ")

    if (order in menu):
        print("You have ordered a",order)
        clarification = input("is that correct?")

        if (clarification in yes_list):
            for x in menu:
                for y in price:
                        print("The price of your order is",price)
                        break

    else:
        print("Sorry, that is not a valid item.")
            
        
