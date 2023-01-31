import math
x_sqr_m_vineyard = int(input())
y_grape_per_sqr = float(input())
z_needed_lt_wine = int(input())
number_of_workers = int(input())

total_grape = x_sqr_m_vineyard * y_grape_per_sqr
wine = (0.40 * total_grape) / 2.5

diff_wine = abs(z_needed_lt_wine - wine)

if wine < z_needed_lt_wine:
    print(f"It will be a tough winter! More {math.floor(diff_wine)} liters wine needed.")
elif wine >= z_needed_lt_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    left_wine = wine - z_needed_lt_wine
    wine_per_worker = left_wine / number_of_workers
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")

