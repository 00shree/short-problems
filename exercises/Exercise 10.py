

print("Enter your birthdate: ")
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

print("Enter today's date: ")
year2 = int(input("Year: "))
month2 = int(input("Month: "))
day2 = int(input("Day: "))

days_year1 = ((year2*365)+(month2*30)+day2)
days_year2 = ((year*365)+(month*30)+day)
days_alive = days_year1 - days_year2
time_slept = days_alive*8

print("You have been alive for:",days_alive,"days.")
print("You have slept for",time_slept,"hours.")



