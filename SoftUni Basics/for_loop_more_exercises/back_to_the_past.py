money = float(input())
years = int(input())

years_old = 18
total_money_left = money



for i in range(1800, years + 1):
    if i % 2 == 0:
        spend_even_year = 12000
        total_money_left = total_money_left - spend_even_year
        years_old += 1

    elif i % 2 != 0:
        spend_odd_year = 12000 + (50 * years_old)
        total_money_left = total_money_left - spend_odd_year
        years_old += 1

if total_money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {total_money_left:.2f} dollars left.")
elif total_money_left < 0:
    abs_money_needed = abs(total_money_left)
    print(f"He will need {abs_money_needed:.2f} dollars to survive.")
