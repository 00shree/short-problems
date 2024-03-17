## Shree Patel
## 709467
## ICS3UO-C
## Exercise 8 High or Low
## 1/16/2023

import random

def Rules():
    global turns
    turns = 1
    global total_points
    
    total_points = 1000*turns
    print(total_points)

    prediction_true = False

    print("High Low Game")
    print()
    print("RULES")
    print("Numbers 1 through 6 are low.")
    print("Numbers 8 through 13 are high.")
    print("7 is neither low nor high")
    print()
    print("You have",total_points,"points.")
    print()
    Loop()

def Loop():
    global total_points
    global turns
    while (total_points != 0):
        risked_points = int(input("Enter the points to risk: "))
        prediction = int(input("Prediction <1=High, 0=Low>:"))

        high_or_low = (random.randint(1,13))

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


        print("Number is ",high_or_low)

        if (prediction == True):
            turns+=1
            total_points *= turns
            print("You win. Total points: ",total_points)
            
        else:
            total_points -= risked_points
            print("You lose. Total points: ",total_points)




        if (total_points > 0):
            restart = input("Would you like to try again? ")
            
            if (restart == "y"):
                Loop()
            else:
                exit()

        elif (total_points == 0):
            print("Gameover.")
            break


Rules()

        


