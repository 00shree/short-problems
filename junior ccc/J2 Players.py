
num_players = int(input("Enter the number of players: "))
count = 0

num_star = 0

while (count < num_players):
    
    num_points = int(input("Enter the points: "))
    num_foul = int(input("Enter the fouls: "))
    score = (num_points * 5) - (num_foul * 3)

    if (score > 40):
        num_star += 1   
    count += 1

if (num_star == num_players):
    print((str(num_players))+"+")

else:
    print(num_star)
