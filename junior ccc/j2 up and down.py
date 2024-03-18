eligible_list = ["I", "O", "S", "H", "Z", "X", "N",] ## make a list of all eligible letters

count = (0) # set eligible letter counter to 0
is_in_list = False

word = input("") # input word and capitalize all letters
capital_word = word.upper()

for c in (capital_word): # for every letter in the capital word
    if (c in eligible_list): # if the letter is in the eligible list, counter will add 1
        count += 1
    elif (c not in eligible_list):  # else, the loop continues
        continue

# if the counter is the same length as the word, it means that all the letters are in the eligible list
if (count == len(capital_word)): # this means the word is rotatable
    print("YES") # therefore returning "YES"

# if the counter is not the same length as the word, it means that not every letter is in the eligible list
elif (count != len(capital_word)): # this means the word is not rotatable
    print("NO") # therefore returning "NO"
    

    

    

    
