
import math

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

while (num2 > 0):
    temp = num1 % num2
    num1 = num2
    num2 = temp

    if (temp == 0):
        print("The GCD is ", num1)

##    print("temp = ", temp)
##    print("num1 = ", num1)
##    print("num2 = ", num2)



