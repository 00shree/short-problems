

time = int(input("Enter the time in minutes: "))

hours = time//60
minutes = time%60

if minutes >= 10:
    print("The time is:",hours,":",minutes)

else:
    minutes = (time%60)%60
    print("The time is:",hours,":",minutes)

