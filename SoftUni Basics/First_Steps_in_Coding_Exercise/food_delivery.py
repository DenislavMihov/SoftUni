chicken_menu_count = int(input())
fish_menu_count = int(input())
vegi_menu_count = int(input())

price_chicken = chicken_menu_count * 10.35
price_fish = fish_menu_count * 12.40
price_vegi = vegi_menu_count * 8.15

all_price_menu = price_chicken + price_fish + price_vegi
desert_price = all_price_menu * 0.2
total_sum = all_price_menu + desert_price +2.5

print(total_sum)

