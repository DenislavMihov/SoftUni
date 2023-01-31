import math
number_of_tournaments = int(input())
init_points = int(input())

total_points = 0 + init_points
w = 0
f = 0
sf = 0

for i in range(1, number_of_tournaments + 1):
    tournament_stage = input()


    if tournament_stage == "W":
        total_points += 2000
        w += 1

    elif tournament_stage == "F":
        total_points += 1200
        f += 1

    elif tournament_stage == "SF":
        total_points += 720
        sf += 1

average_points = (total_points - init_points) / number_of_tournaments
percent_winnings = (w / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)} ")
print(f"{percent_winnings:.2f}%")
