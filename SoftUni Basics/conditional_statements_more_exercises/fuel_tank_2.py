fuel = input()
qty_fuel = float(input())
club_card = input()

# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър

gasoline_price = qty_fuel * 2.22
diesel_price = qty_fuel * 2.33
gas_price = qty_fuel * 0.93

gas_price_with_card = (0.93 - 0.08) * qty_fuel
gasoline_price_with_card = qty_fuel * (2.22 - 0.18)
diesel_price_with_card = qty_fuel * (2.33 - 0.12)




if fuel == "Gas":
    if club_card == "Yes" and qty_fuel < 20:
        print(f"{gas_price_with_card:.2f} lv.")
    elif club_card == "Yes" and 25 >= qty_fuel >= 20:
        print(f"{gas_price_with_card * 0.92 :.2f} lv.")
    elif club_card == "Yes" and qty_fuel > 25:
        print(f"{gas_price_with_card * 0.9 :.2f} lv.")
    elif club_card == "No" and qty_fuel < 20:
        print(f"{gas_price:.2f} lv.")
    elif club_card == "No" and 25 >= qty_fuel >= 20:
        print(f"{gas_price * 0.92:.2f} lv.")
    elif club_card == "No" and qty_fuel > 25:
        print(f"{gas_price * 0.9:.2f} lv.")
elif fuel == "Gasoline":
    if club_card == "Yes" and qty_fuel < 20:
        print(f"{gasoline_price_with_card:.2f} lv.")
    elif club_card == "Yes" and 25 >= qty_fuel >= 20:
        print(f"{gasoline_price_with_card * 0.92 :.2f} lv.")
    elif club_card == "Yes" and qty_fuel > 25:
        print(f"{gasoline_price_with_card * 0.9 :.2f} lv.")
    elif club_card == "No" and qty_fuel < 20:
        print(f"{gasoline_price:.2f} lv.")
    elif club_card == "No" and 25 >= qty_fuel >= 20:
        print(f"{gasoline_price * 0.92:.2f} lv.")
    elif club_card == "No" and qty_fuel > 25:
        print(f"{gasoline_price * 0.9:.2f} lv.")
elif fuel == "Diesel":
    if club_card == "Yes" and qty_fuel < 20:
        print(f"{diesel_price_with_card:.2f} lv.")
    elif club_card == "Yes" and 25 >= qty_fuel >= 20:
        print(f"{diesel_price_with_card * 0.92 :.2f} lv.")
    elif club_card == "Yes" and qty_fuel > 25:
        print(f"{diesel_price_with_card * 0.9 :.2f} lv.")
    elif club_card == "No" and qty_fuel < 20:
        print(f"{diesel_price:.2f} lv.")
    elif club_card == "No" and 25 >= qty_fuel >= 20:
        print(f"{diesel_price * 0.92:.2f} lv.")
    elif club_card == "No" and qty_fuel > 25:
        print(f"{diesel_price * 0.9:.2f} lv.")

