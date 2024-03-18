## Generates hailstone numbers based on fibbonacci sequence
integer = 1
loopcounter = 0
counter = 1

while (counter < 200):
    integer = counter

    while (True):
        if (integer % 2 == 0):
            integer //= 2

        elif (integer % 2 == 1):
            integer = (integer * 3) + 1

        if (integer == 1):
            loopcounter += 1
            counter += 1
            print("The number", counter ,"ends with the Hailstones pattern 4, 2, 1")
            break
        
if (counter != loopcounter):
    print("All numbers end with the pattern 4, 2, 1")
else:
    print("Not all numbers end with the pattern 4, 2, 1")

