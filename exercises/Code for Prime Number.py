

def isPrime(number):
####    number=int(input("Give a number: "))
##
##    if (number==1):
##         return print(number,"is not prime")
##    else:
##        divisor = 2
        division_occured=False
        divisor=2
        while(divisor <= number//2):
            if(number%divisor == 0):
                division_occured=True
              #   print(number,"not prime")
                break
            divisor+=1

    #if(division_occured==False):
       # print(number,"is prime")
        return division_occured

num=int(input("Give a number: "))
check=isPrime(num)
if(check==False):
    print(num, "is prime.")
else:
    print(num,"is not prime.")
