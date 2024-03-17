bad_pairs = False
good_pairs = True
pairs = {}

num = int(input("enter number of students: "))
first_set = input("enter the first set: ")
second_set = input("enter the second set: ")

first_split = first_set.split()
second_split = second_set.split()

for char in first_split:
    index1 = first_split.index(char)
    index2 = second_split[index1]

    pairs.update({char: index2})

for person in first_split:
    partner = pairs[person]

    if partner == person or pairs[partner] != person:
        good_pairs = False
        break


if good_pairs:
    print("good")
else:
    print("bad")
