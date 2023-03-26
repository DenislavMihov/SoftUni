items = {"shards": 0, "fragments": 0, "motes": 0}
line = input().split()
obtained = False
while not obtained:

    for index in range(0, len(line), 2):
        value = int(line[index])
        key = line[index + 1].lower()
        if key not in items:
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            items[key] -= 250
            print("Shadowmourne obtained!")
            obtained = True
        elif items["fragments"] >= 250:
            items[key] -= 250
            print("Valanyr obtained!")
            obtained = True
        elif items["motes"] >= 250:
            items[key] -= 250
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break
    if obtained:
        break
    line = input().split()

for material, quantity in items.items():
    print(f"{material}: {quantity}")