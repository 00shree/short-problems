

model = int(input("Enter the car's model: "))

while (model > 0):   
    if ((model == 119) or (model == 179) or (model == 221) or (model == 780) or (189 >= model >= 195)):
        print("Your car is defective. It must be repaired.")
        break
    else:
        print("Your car is not defective.")
        break

    if (model == 0):
        break
        

    
