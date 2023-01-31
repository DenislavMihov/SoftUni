price_per_kilo_vegi = float(input())
price_per_kilo_fruit = float(input())
kilos_vegi = int(input())
kilos_fruit = int(input())

vegi_cost = price_per_kilo_vegi * kilos_vegi
fruits_cost = price_per_kilo_fruit * kilos_fruit

whole_cost_in_euro =  (vegi_cost + fruits_cost) / 1.94
print(f"{whole_cost_in_euro:.2f}")


