import randint from random

yes_list = ["y","yes","Yes"]
tries = 0


global is_low
global is_high
global is_neither
global current_points
global tries

is_low = False
is_high = False
is_neither = False
win = False
loss = False

current_points = 1000

def Intro():    
    global current_points
    global tries
    current_points = current_points
    tries += 1

    while (current_points > 0):
        print ("High Low Game")
        print("")
        print("RULES")
        print("Numbers 1 through 6 are low")
        print("Numbers 8 through 13 are high")
        print("Number 7 is neither high or low")
        print("")
        print("You have",current_points,"points.")
        Main()

    if (current_points == 0):
        break
        print("You've run out of points.")
        print("You had",tries,"tries.")


def Main():
    global current_points
    global is_neither
    global is_low
    global is_high
    global win
    global loss
    
    current_points = current_points

    risk_points = int(input("Enter points to risk: "))
    prediction = int(input("Predict <1=High, 0=Low>: "))

    random_int = (random.randint(1,14))
    print(random_int)

    if (1 <= random_int <= 6):
        is_low = True
    elif (8 <= random_int <= 13):
        is_high = True
    elif (random_int == 7):
        is_neither = True



    if (prediction == 1):
        if (is_neither == True) or (is_low == True):
            loss = True
        if (is_high == True):
            win = True

    if (prediction == 0):
        if (is_neither == True) or (is_high == True):
            loss = True
        if (is_low == True):
            win = True

    if (win == True):
        current_points *= 2
        print("The number is",random_int)
        print("You win.")
        print("You have",current_points,"points.")

    elif (loss == True):
        current_points -= risk_points
        print("The number is",random_int)
        print("You lost.")
        print("You have",current_points,"points.")

    try_again = input("Play again? ")

    if (try_again in yes_list):
        Intro()
    else:
        print("goodbye")
        exit()


        
Intro()               
 

        
        
            
        
        
    
                     
    

            

    
