import re

n = int(input())
pattern = r"^\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#$"

for i in range(n):
    boss_input = input()
    match = re.match(pattern, boss_input)
    if match:
        boss_name = match.group(1)
        title = match.group(2)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")