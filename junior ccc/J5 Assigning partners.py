bad_pairs = False
good_pairs = False
pairs = {}

num = int(input("enter number of students: "))
first_set = input("enter the first set: ")
second_set = input("enter the second set: ")

first_split = first_set.split()
second_split = second_set.split()

for char in first_split:
    index1 = first_split.index(char)
    index2 = second_split[index1]

    pairs.update({char:index2})

##print(pairs)

for person in first_split:
##    print(x,partner)
    partner = pairs[person]
    reverse_pair = second_split[partner]

    
    if (partner == person)or(reverse_pair == person):
        bad_pairs = (True)
    else:
        good_pairs = (True)


if (good_pairs == True):
    print("good")
elif (bad_pairs == True):
    print("bad")
        

    
    
    

    
        
    



        
