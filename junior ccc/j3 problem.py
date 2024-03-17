letters_list = []
number_list = []
sign_list = []

sequence = input("Enter the sequence: ")

n = 0

while n < len(sequence):
    c = sequence[n]
    
    if c.isalpha():
        cluster = ""
        while n < len(sequence) and sequence[n].isalpha():
            cluster += sequence[n]
            n += 1
        letters_list.append(cluster)
    elif c.isdigit() or c in ('+', '-'):
        sign = ''
        while n < len(sequence) and (sequence[n].isdigit() or sequence[n] in ('+', '-')):
            sign += sequence[n]
            n += 1
        sign_char = sign[0]
        sign_list.append(sign_char)
        number_list.append(int(sign[1:]))

for i in range(len(letters_list)):
    action = "tighten" if sign_list[i] == '+' else "loosen"
    print(f"{letters_list[i]} {action} {number_list[i]}")
