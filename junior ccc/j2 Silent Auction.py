name_list = []
bid_list = []


num_people = int(input(""))

for x in range(num_people):
    name = input("")
    name_list.append(name)
    
    bid = int(input(""))
    bid_list.append(bid)
    

##print(bid_list)
##print(name_list)

max_bid = max(bid_list)

bid_index = bid_list.index(max_bid)
name_index = name_list[bid_index]


print(name_index)

        
        



        
        
    
