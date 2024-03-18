#Generates every prime number between two inputted numbers of the range
low=int(input("What is the low end of the range: "))
high=int(input("What is the high end of the range: "))
print("Prime numbers in the given range are: ",end="")

##number=low
if (low==1):
        low=2
for number in range(low,(high+1)):
##    if (number==1):
##        number=2
    
    divisor = 2
    division_occured=False

    while(divisor <= number//2):
        if(number%divisor == 0):
            division_occured=True
            break
        divisor+=1

    if(division_occured==False):
        print(number, end=" ")
#    number+=1
