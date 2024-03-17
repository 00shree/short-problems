def main():

    percentage = int(input("Enter the percentage: "))

    if percentage >= 90 <= 100:
        print("The corresponding letter grade is: A")

    elif percentage >= 80 <= 89:
        print("The corresponding letter grade is: B")

    elif percentage >= 70 <= 79:
        print("The corresponding letter grade is: C")

    elif percentage >= 60 <= 69:
        print("The corresponding letter grade is: D")

    else:
        print("The corresponding letter grade is: F")


    restart = input("Would you like to restart? ")

    if restart == "yes":
        main()

    else:
        exit()

main()
        
        
