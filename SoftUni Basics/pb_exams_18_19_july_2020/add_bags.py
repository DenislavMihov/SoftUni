price_of_bags_over_20_kilos = float(input())
kilos_of_bags = float(input())
days_to_tripping = int(input())
number_of_bags = int(input())

price_of_bags = 0

if kilos_of_bags < 10:
    price_of_bags = price_of_bags_over_20_kilos * 0.2
    if days_to_tripping < 7:
        price_of_bags = price_of_bags + (price_of_bags * 0.4)
    elif days_to_tripping <= 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.15)
    elif days_to_tripping > 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.1)

elif kilos_of_bags <= 20:
    price_of_bags = price_of_bags_over_20_kilos * 0.5

    if days_to_tripping < 7:
        price_of_bags = price_of_bags + (price_of_bags * 0.4)
    elif days_to_tripping <= 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.15)
    elif days_to_tripping > 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.1)

else:
    price_of_bags = price_of_bags_over_20_kilos

    if days_to_tripping < 7:
        price_of_bags = price_of_bags + (price_of_bags * 0.4)
    elif days_to_tripping <= 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.15)
    elif days_to_tripping > 30:
        price_of_bags = price_of_bags + (price_of_bags * 0.1)

total_sum = price_of_bags * number_of_bags

print(f"The total price of bags is: {total_sum:.2f} lv. ")