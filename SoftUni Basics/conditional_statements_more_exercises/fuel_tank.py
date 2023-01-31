fuel = input()
lt_fuel_left = int(input())

if fuel == "Diesel":
    if lt_fuel_left >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
elif fuel == "Gasoline":
    if lt_fuel_left >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")
elif fuel == "Gas":
    if lt_fuel_left >= 25:
        print(f"You have enough {str.lower(fuel)}.")
    else:
        print(f"Fill your tank with {str.lower(fuel)}!")

else:
    print("Invalid fuel!")
