print("Number of daytime minutes? ") # ask for input for the number of daytime minutes from the user
daytime = int(input(""))
print("Number of evening minutes? ") # ask for input for the nummber of evening minutes from the user
evening = int(input(""))
print("Number of weekend minutes? ") # ask for input for the number of weekend minutes from the user
weekend = int(input(""))

# PLAN A: if the daytime mins is more than 100, the user has to pay for additional minutes after 100
if (daytime > 100):
    plan_a = ((daytime - 100) * 0.25) + (0.15 * evening) + (0.20 * weekend)
# PLAN A: if the daytime mins is less than or equal 100, it will be free so user only has to pay for evenings and weekeends
elif (daytime <= 100):
    plan_a = (0.15 * evening) + (0.20 * weekend)
    
# PLAN B: if the daytime mins is more than 250, the user has to pay for additional minutes after 250
if (daytime > 250):
    plan_b = ((daytime - 250) * 0.45) + (0.35 * evening) + (0.25 * weekend)
# PLAN B: if the daytime minutes is less than or equal ro 250, they will be free so the user only has to pay for evenings and weekends
elif (daytime <= 250):
    plan_b = (0.35 * evening) + (0.25 * weekend)    


# if PLAN A cost is greater than the PLAN B cost, PLAN B is cheaper, vice versa
if (plan_a > plan_b):
    cheapest = ("Plan B is cheapest.")
elif (plan_b < plan_a):
    cheapest =("Plan A is cheapest")

# print each costs and which is cheapest 
print("Plan A costs", plan_a)
print("Plan B costs", plan_b)
print(cheapest)
