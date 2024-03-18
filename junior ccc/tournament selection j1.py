score_list = [] # SET A SCORE LIST to add all the wins and loss scores

# Set win and loss counter
win_count = 0
loss_count = 0

# make a for loop to iterate 6 times for all six score inputs from the player 
for x in range(6):
    win_loss = input("")
    score_list.append(win_loss)


# set a for loop for each element in the list, if the score is W, the win counter increases by one
for c in score_list:
    if c == "W":
        win_count += 1
# if the score is L the loss counter increases by one
    elif c == "L":
        loss_count += 1

# if the win counter is 5 or 6, the output will be group one, group two if the score is 3 or 4, and group 3 if the score is 1 or 2
if (win_count == 5) or (win_count == 6):
    print("1")

elif (win_count == 3) or (win_count == 4):
    print("2")

elif (win_count == 1) or (win_count == 2):
    print("3")

    

    
