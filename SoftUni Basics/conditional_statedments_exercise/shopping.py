budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

price_of_vc = video_card_count * 250
price_of_processor = processor_count * (price_of_vc * 0.35)
price_of_ram = ram_count * (price_of_vc * 0.10)

total_price = 0
if video_card_count > processor_count:
    total_price = (price_of_vc + price_of_processor + price_of_ram) * 0.85
else:
    total_price = price_of_vc + price_of_processor + price_of_ram

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

