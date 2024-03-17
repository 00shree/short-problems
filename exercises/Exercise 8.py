

first_integer = int(input("Enter an integer: "))
second_integer = int(input("Enter a second integer: "))

first_modulus = first_integer / second_integer
first_division = first_integer % second_integer

second_modulus = second_integer / first_integer
second_division = second_integer % first_integer

print(first_integer,"%",second_integer,"=",first_modulus)
print(first_integer,"/",second_integer,"=",first_division)
print()
print(second_integer,"%",first_integer,"=",second_modulus)
print(second_integer,"/",first_integer,"=",second_division)
