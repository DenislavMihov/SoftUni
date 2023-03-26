countries = input().split(", ")
capitals = input().split(", ")
pairs = {}

for i in range(len(countries)):
    pairs[countries[i]] = capitals[i]

for country, capital in pairs.items():
    print(f"{country} -> {capital}")