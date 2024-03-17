##ICS3UO-C
##Mr Veera
##Shree Patel
##2022-09-30
##Exercise 3 page 99 Adobe Reader


def main():
    
    rent = int(input("Enter your yearly rent fees: "))
    food_and_drinks = int(input("Enter your yearly food and drinks fees: "))
    transportation = int(input("Enter your yearly transportation fees: "))
    additional_fees = int(input("Enter any additional fees: "))

        
    scholarship = input("Are you under a scholarship? ")


    if scholarship == "yes":
        total_cost = rent+food_and_drinks+transportation+additional_fees
        print("Your total college fees calculate to:",total_cost,"dollars.")
    elif scholarship == "no":
        tuition = int(input("Enter your yearly tuition fees: "))
        total_cost = tuition+rent+food_and_drinks+transportation+additional_fees
        print("Your total college fees calculate to:",total_cost,"dollars per year.")
    else:
        print("Invalid input. Please answer with either 'yes' or 'no'.")
        main()

    restart = input("Would you like to try again?" )

    if restart == "yes":
        main()
    else:
        exit()

main()


