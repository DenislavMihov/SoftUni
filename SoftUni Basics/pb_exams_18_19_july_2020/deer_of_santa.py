import math
days = int(input())
food = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

deer_1 = first_deer_food_per_day * days
deer_2 = second_deer_food_per_day * days
deer_3 = third_deer_food_per_day * days

total_needed_food = deer_1 + deer_2 + deer_3

diff = abs(food - total_needed_food)


if total_needed_food <= food:
    print(f"{math.floor(diff)} kilos of food left.")

else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")



