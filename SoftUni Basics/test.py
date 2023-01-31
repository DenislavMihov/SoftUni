import math

cat_breed = input()
cat_gender = input()
life_expectancy = 0

if cat_breed == 'British Shorthair':
    if cat_gender == 'm':
        life_expectancy = 13
    elif cat_gender == 'f':
        life_expectancy = 14

elif cat_breed == 'Siamese':
    if cat_gender == 'm':
        life_expectancy = 15
    elif cat_gender == 'f':
        life_expectancy = 16

elif cat_breed == 'Persian':
    if cat_gender == 'm':
        life_expectancy = 14
    elif cat_gender == 'f':
        life_expectancy = 15

elif cat_breed == 'Ragdoll':
    if cat_gender == 'm':
        life_expectancy = 16
    elif cat_gender == 'f':
        life_expectancy = 17

elif cat_breed == 'American Shorthair':
    if cat_gender == 'm':
        life_expectancy = 12
    elif cat_gender == 'f':
        life_expectancy = 13

elif cat_breed == 'Siberian':
    if cat_gender == 'm':
        life_expectancy = 11
    elif cat_gender == 'f':
        life_expectancy = 12

    # life_expectancy_months = math.floor(life_expectancy * 12 / 6)
    # print(f"{life_expectancy_months} cat months")
elif cat_breed == ['British Shorthair', 'Siamese', 'Persian', 'Ragdoll', 'American Shorthair', 'Siberian']:
    life_expectancy_months = math.floor(life_expectancy * 12 / 6)
    print(f"{life_expectancy_months} cat months")
else:
    print("Tom is invalid cat!")