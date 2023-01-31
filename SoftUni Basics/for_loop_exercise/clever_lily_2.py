age = int(input())
price_wash_machine = float(input())
toy_price = int(input())

brother_count = 0
count_toys = 0
total_sum = 0
money = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys = count_toys + 1
    else:
        brother_count += 1
        money = money + 10
        total_sum = total_sum + money

result = (count_toys * toy_price) + total_sum - brother_count

diff = abs(result - price_wash_machine)
if result >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")