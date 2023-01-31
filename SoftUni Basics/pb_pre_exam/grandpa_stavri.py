num_days = int(input())

total_liters_rakia = 0
total_degrees = 0

for i in range(1, num_days + 1):
    qty_rakia = float(input())
    degrees = float(input())

    total_liters_rakia += qty_rakia
    total_degrees = total_degrees +  (qty_rakia * degrees)

average_degrees = total_degrees / total_liters_rakia

print(f"Liter: {total_liters_rakia:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")


