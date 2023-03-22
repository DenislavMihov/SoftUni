import re


pattern = r"^>>([A-Za-z]+)<<(\d+(\.?\d*)?)!(\d+)$"
total_price = 0
bought_items = []
while True:
    command = input()
    if command == "Purchase":
        break

    match = re.findall(pattern, command)
    if not match:
        continue

    groups = match[0]

    item = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])

    bought_items.append(item)
    total_price += quantity * price


print("Bought furniture:")
print("\n".join(bought_items))
print(f"Total money spend: {total_price:.2f}")

