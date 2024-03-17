
amount = int(input("Enter the amount: "))
years = int(input("Enter the number of years: "))
interest = int(input("Enter the interest rate: "))

principal = amount/(1+years*interest)
print("The principal amount is:",principal)
