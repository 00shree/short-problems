a_count = 0
b_count = 0

num = int(input("enter number of letters: "))
letters = input("enter the letters: ")

for x in letters:
    if (x == "A"):
        a_count += 1
    elif (x == "B"):
        b_count += 1

if (a_count > b_count):
    print("A")
elif (b_count > a_count):
    print("B")
elif (a_count == b_count):
    print("Tie")
    
    
    
