import math
number_of_days = int(input())
left_food_in_kilograms = int(input())
dog_food_per_day_in_kilograms = float(input())
cat_food_per_day_in_kilograms = float(input())
turtle_food_per_day_in_grams = float(input())

dog_needed_food = number_of_days * dog_food_per_day_in_kilograms
cat_needed_food = number_of_days * cat_food_per_day_in_kilograms
turtle_needed_food = number_of_days * (turtle_food_per_day_in_grams / 1000)
total_food_needed = dog_needed_food+ cat_needed_food + turtle_needed_food

diff = abs(left_food_in_kilograms - total_food_needed)

if total_food_needed <= left_food_in_kilograms:
    print(f"{math.floor(diff)} kilos of food left.")
elif total_food_needed > left_food_in_kilograms:
    print(f"{math.ceil(diff)} more kilos of food are needed.")