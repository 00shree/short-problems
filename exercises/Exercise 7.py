

def main:
    
    yes_list = {"Yes","yes","y"}
    number = input("Enter a positive three-digit number: ")

    if number == int:     
        hundreds_place = (number % 1000) // 100
        tens_place = (number % 100) // 10
        ones_place = number % 10

        print("The hundreds-place digit is:",hundreds_place)
        print("The tens-place digit is:",tens_place)
        print("The ones-plave digit is:",ones_place)

    elif number <= 0
        print("The integer must be positive.")

    else:
        print("Invalid input, please enter an integer value.")

    restart = input("Would you like to restart?")

    if restart in yes_list:
        main()

    else:
        print("Goodbye.")
        exit()

main()
