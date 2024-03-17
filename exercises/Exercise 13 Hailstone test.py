
RANGE_END = 200
RANGE_START = 1
loopcounter = 0
counter = 1

while (counter < RANGE_END):
    RANGE_START = counter

    while (True):
        if (RANGE_START % 2 == 0):
            RANGE_START //= 2

        elif (RANGE_START % 2 == 1):
            RANGE_START = (RANGE_START * 3) + 1

        if (RANGE_START == 1):
            loopcounter += 1
            counter += 1
            print("The number, ", counter ,"ends with the Hailstones pattern 4, 2, 1")
            break
        
if (counter != loopcounter):
    print("All numbers end with the pattern 4, 2, 1")
else:
    print("Not all numbers end with the pattern 4, 2, 1")

