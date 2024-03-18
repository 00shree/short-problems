is_triangle = False
output = ("")

angle1 = int(input(""))
angle2 = int(input(""))
angle3 = int(input(""))


if (angle1 + angle2 + angle3) == 180:
    is_triangle == True
    
if (angle1 == angle2) and (angle2 == angle3):
    output = ("Equilateral")
elif (angle1 + angle2 + angle3) != 180:
    output = ("Error")
    
if (is_triangle == True):
    if (angle1 == angle2) or (angle2 == angle3):
        output = ("Isosceles")
    else:
        output =  ("Scalene")

print(output)
        
    
    

