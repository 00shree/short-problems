
def main():

    yes_list = ["Yes","yes","y"]
    burgers = int(input("Enter the number of burgers: "))
    fries = int(input("Enter the number of fries: "))
    sodas = int(input("Enter the number of sodas: "))

    burgers_cost = burgers*(1.69)
    fries_cost = fries*(1.09)
    sodas_cost = sodas*(0.99)

    total_before_tax = sodas_cost + fries_cost + burgers_cost
    tax = (6.5*total_before_tax)/100
    final_total = total_before_tax + tax

    print("Total before tax:","$",total_before_tax)
    print("Tax:","$",tax)
    print("Final total:","$",final_total)

    tendered_amount = float(input("Enter amount tendered: $"))

    if tendered_amount >= final_total:
        change = tendered_amount - final_total
        print("Change:","$",change)
    else:
        print("Insufficient funds, please enter an amount greater than your total.")
        restart = input("Would you like to restart? ")

    if restart in yes_list:
        
        main()     
    else:
        
        exit()

main()
