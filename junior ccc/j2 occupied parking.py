yesterday_list = []
today_list = []
spots_occupied = 0

spots = int(input(""))
yesterday = input("")
today = input("")


for y in (yesterday):
    yesterday_list.append(y)

for t in (today):
    today_list.append(t)

print(today_list)
print(yesterday_list)

for e in (yesterday_list):
    for c in (today_list):
        if (c == "C" and e == "C"):
            spots_occupied += 1

            


print(spots_occupied)


    
