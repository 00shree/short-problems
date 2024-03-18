# Shree Patel
# 709467
# ICS2O0A
# College Fees Canculator
# Mr Veera
# 19 Nov 2021

scholarship=float(input("Enter your yearly scholarship expenses in $:"))
rent_and_other_bills=float(input("Enter your yearly rent and other billing fees in $:"))
school_supplies=float(input("Enter your yearly school books and other equipment expenses in $:"))
parking_fees=float(input("Enter your yearly parking fees in $:"))
food=float(input("Enter your yearly expenses for food in $:"))
income=float(input("Enter your yearly salary for the total of any jobs you are working in $:"))
tuition=float(input("Enter your yearly tuition fees in $:"))

total=(rent_and_other_bills+school_supplies+parking_fees+food+tuition)-(scholarship+income)

print("Your total college fees incuding scholarship, rent as well as any other billing expenses, school supplies, parking fees, food, income and tuition is: ",total)
