split_instructions = []
letters_list = []
number_list = []
sign_list = []

sequence = input("Enter the sequence: ")


for c in sequence:
    if (c == "+"):
        placement = sequence.index(c)
        sign_list.append("tighten")
        
        sign_index = sequence.index(c)
        number_index = (sign_index + 1)
        number = sequence[number_index]
        number_list.append(number)

    elif (c == "-"):
        placement = sequence.index(c)
        sign_list.append("loosen")
        
        sign_index = sequence.index(c)
        number_index = (sign_index + 1)
        number = sequence[number_index]
        number_list.append(number)

print(number_list)
print(sign_list)



        
