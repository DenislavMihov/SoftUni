price_of_pack_of_dogs_food = 2.50
price_of_pack_of_cats_food  = 4

number_of_packs_of_dogs_food = int(input())
number_of_packs_of_cats_food = int(input())

cost = (price_of_pack_of_dogs_food * number_of_packs_of_dogs_food) + \
       (price_of_pack_of_cats_food * number_of_packs_of_cats_food)

print(f"{cost} lv.")



