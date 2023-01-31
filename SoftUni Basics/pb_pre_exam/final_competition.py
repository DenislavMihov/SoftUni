num_dancers = int(input())
numb_points = float(input())
season = input()
place = input()

earned_money = 0

if place == "Bulgaria":
    earned_money = num_dancers * numb_points

    if season == "summer":
        earned_money = earned_money * 0.95
    elif season == "winter":
        earned_money = earned_money * 0.92

elif place == "Abroad":
    earned_money = (num_dancers * numb_points) * 1.5

    if season == "summer":
        earned_money = earned_money * 0.9
    elif season == "winter":
        earned_money = earned_money * 0.85

charity = earned_money * 0.75

lefted_money = earned_money - charity
money_per_dancer = lefted_money / num_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
