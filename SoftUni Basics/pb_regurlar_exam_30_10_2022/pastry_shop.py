sweet = input()
qty_of_sweets = int(input())
day_of_month = int(input())

total_cost = 0
mid_sum = 0

if sweet == "Cake":

    if day_of_month <= 15:
        mid_sum = qty_of_sweets * 24

    elif day_of_month > 15:
        mid_sum = qty_of_sweets * 28.70

if sweet == "Souffle":

    if day_of_month <= 15:
        mid_sum = qty_of_sweets * 6.66

    elif day_of_month > 15:
        mid_sum = qty_of_sweets * 9.80

if sweet == "Baklava":

    if day_of_month <= 15:
        mid_sum = qty_of_sweets * 12.6

    elif day_of_month > 15:
        mid_sum = qty_of_sweets * 16.98

if day_of_month <= 22:

    if mid_sum >= 100 and mid_sum < 200:
        mid_sum = mid_sum * 0.85
    elif mid_sum > 200:
        mid_sum *= 0.75

if day_of_month <= 15:
    mid_sum *= 0.9

print(f"{mid_sum:.2f}")
