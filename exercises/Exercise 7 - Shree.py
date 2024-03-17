

## Defining the main code in which the program will loop.
def main():

    try:
            yes_list = {"Yes","yes","y"} ## A list that defines the inputs resulting in a loop.
            number = int(input("Enter a positive three-digit number: ")) ## Inputting an integer value from the user.


            ## Checking if the inputted value is a three-digit number, if so, the computations are done.
            if number >= 100:
                hundreds_place = (number % 1000) // 100
                tens_place = (number % 100) // 10
                ones_place = number % 10

                print("The hundreds-place digit is:",hundreds_place)
                print("The tens-place digit is:",tens_place)
                print("The ones-place digit is:",ones_place)

            ## If the inputted number is not a three-digit number, the computer will inform the user.
            else:
                print("Please enter a number with 3 digits.")

            ## If the inputted value is not a positive number, the computer will inform the user.
            if number < 0:
                print("Please enter an integer value greater than 0.")

    ## If the inputted value is not a number at all, the computer will inform the user.
    except(ValueError):
        print("Invalid input. Please enter an integer number value.")

    ## Regardless of the outputs, the computer will ask the user if they wish to restart the program.
    restart = input("Would you like to restart? ")

    ## If the input is within the 'Yes list', the program will restart, otherwise it will end.
    if restart in yes_list:
        main()

    else:
        print("Goodbye.")
        exit()

main()
