shift_list = []
final_sum = 0

num = int(input(""))
shift = int(input(""))
shift_list.append(num)

for x in range(shift+1):
    degree = (10 ** x)
    shifted_num = (num * degree)
    shift_list.append(shifted_num)

for c in (shift_list):
    final_sum += c

print(final_sum)

    
