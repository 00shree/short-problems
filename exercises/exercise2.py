
def main():

    diameter = input("Enter the diameter of the pizza in inches: ")

    if diameter == float:
        total_cost = (diameter*diameter*0.05)+1.75
        print("")
    else:
        print("The diameter of a pizza must be a number.")

    restart=input("Would you like to try again? ")
    if restart == "yes":
        main()
    else:
        exit()

main()
