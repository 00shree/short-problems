apple_1 = int(input(""))
apple_2 = int(input(""))
apple_3 = int(input(""))

banana_1 = int(input(""))
banana_2 = int(input(""))
banana_3 = int(input(""))

total_apple = (apple_1 + apple_2 + apple_3)
total_banana = (banana_1 + banana_2 + banana_3)

if (total_apple > total_banana):
    print("A")

elif (total_banana > total_apple):
    print("B")
