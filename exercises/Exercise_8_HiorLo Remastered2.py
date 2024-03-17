import random

yes_list = ["y", "yes", "Yes", "Y"]
no_list = ["n", "no", "No", "N"]
tries = 0


def Rules():
    global losses
    global wins
    global turns
    global total_points
    global tries
    turns = 1

    total_points = 1000 * turns
    print(total_points)

    prediction_true = False


    print("High Low Game")
    print()
    print("RULES")
    print("Numbers 1 through 6 are low.")
    print("Numbers 8 through 13 are high.")
    print("7 is neither low nor high")
    print()
    print("You have", total_points, "points.")
    print()
    Loop()

def TryAgain():
    global losses
    global tries
    if total_points == 0:
        losses += 1
        print("Wins:",wins)
        print("Losses: ",losses)
        start_over = input("Would you like to start over? ")

        if start_over in yes_list:
            Rules()
        else:
            exit()

    elif total_points > 0:
        try_again = input("Would you like to try again? ")

        if try_again in yes_list:
            Loop()
        else:
            exit()

def Loop():
    global total_points
    global turns
    global losses
    global wins
    global tries
    
    is_low = False
    is_high = False
    neither = False

    losses = 0
    wins = 0

    while total_points != 0:
        try:
            risked_points = int(input("Enter the points to risk: "))
            prediction = int(input("Prediction <1=High, 0=Low>:"))
            tries += 1

            high_or_low = random.randint(1, 13)

            if (prediction == 0):
                is_low = True
            elif (prediction == 1):
                is_high = True

            if (1 <= high_or_low <= 6) and (prediction == 0):
                prediction_true = True
            elif (1 <= high_or_low <= 6) and (prediction == 1):
                prediction_true = False
            elif (8 <= high_or_low <= 13) and (prediction == 0):
                prediction_true = False
            elif (8 <= high_or_low <= 13) and (prediction == 1):
                prediction_true = True
            elif (high_or_low == 7):
                neither = True

            print("Number is", high_or_low)

            if prediction_true:
                wins += 1
                turns += 1
                total_points *= turns
                print("You win. Total points:", total_points)
            else:
                losses += 1
                total_points -= risked_points
                print("You lose. Total points:", total_points)
    

            if total_points == 0:
                print("Game over.")
                print("Your total tries were:", tries)
                

        except ValueError:
            print("Invalid input")
            TryAgain()

Rules()

