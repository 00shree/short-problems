## Shree Patel
## 709467
## ICS3UO-C

parameter = int(input())
encoded_message = input()
new_word = ""

for i in range(len(encoded_message)+1):
    shift = (3 * i) + parameter
    unicode_num = ord(encoded_message[i-1])
    alpha_word = ""
    
    for x in range(shift):
        if unicode_num == 65:
            alpha_word = "Z"
            unicode_num = 90
        else:
            alpha_word = chr(unicode_num - 1)
            unicode_num = ord(alpha_word)

    new_word += alpha_word

print(new_word)
