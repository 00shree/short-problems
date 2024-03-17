string = input("Enter a string: ")

char = 0
message = ''

while (char < len(string)):
    letter = string[char]
    char += 1

    new_uni = ord(letter)+2
    new_char = chr(new_uni)

    message += str(new_char)
    
    if (char == len(string)):
        print("Encoded message:",message)
        break

