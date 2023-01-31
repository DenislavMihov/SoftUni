cat_breed = input()
cat_sex = input()

average_yers = 0
flag = False
if cat_breed == "British Shorthair":
    if cat_sex == "m":
        average_yers = 13
    elif cat_sex == "f":
        average_yers = 14

elif cat_breed == "Siamese":
    if cat_sex == "m":
        average_yers = 15
    elif cat_sex == "f":
        average_yers = 16

elif cat_breed == "Persian":
    if cat_sex == "m":
        average_yers = 14
    elif cat_sex == "f":
        average_yers = 15

elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        average_yers = 16
    elif cat_sex == "f":
        average_yers = 17.

elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        average_yers = 12
    elif cat_sex == "f":
        average_yers = 13
elif cat_breed == "Siberian":
    if cat_sex == "m":
        average_yers = 11
    elif cat_sex == "f":
        average_yers = 12

else:
    print(f"{cat_breed} is invalid cat!")
    flag = True

men_months = average_yers * 12
cats_months = men_months / 6
if not flag:
    print(f"{int(cats_months)} cat months")