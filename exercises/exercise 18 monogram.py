

name = input("Enter your first name: ")
middle = input("Enter your middle initial: ")
last = input("Enter your last name: ")

first_initial = ((name[:1])).lower()
middle_initial = middle.lower()
last_initial = last.upper()

monogram = str(first_initial+middle_initial+last_initial)
print(monogram)
