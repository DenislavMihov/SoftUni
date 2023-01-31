percent_fats = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

fats = ((percent_fats * total_calories) / 9) / 100
protein = ((percent_protein * total_calories) / 4) / 100
carbs = ((percent_carbs * total_calories) / 4) / 100

calories_per_gram = total_calories /  (fats + protein + carbs)
water = (percent_water * calories_per_gram) / 100

left_calories = calories_per_gram - water

print(f"{left_calories:.4f}")
