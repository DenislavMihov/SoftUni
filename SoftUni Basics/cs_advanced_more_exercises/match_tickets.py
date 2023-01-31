budget = float(input())
category = input()
number_of_people = int(input())


money_left_for_tickets = 0
price_of_tickets = 0

if category == "Normal":
    price_of_tickets = 249.99 * number_of_people
    if number_of_people <= 4:
        money_left_for_tickets = budget * 0.25
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 9:
        money_left_for_tickets = budget * 0.4
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 24:
        money_left_for_tickets = budget * 0.5
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 49:
        money_left_for_tickets = budget * 0.6
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people >= 50:
        money_left_for_tickets = budget * 0.75
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
elif category == "VIP":
    price_of_tickets = 499.99 * number_of_people
    if number_of_people <= 4:
        money_left_for_tickets = budget * 0.25
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 9:
        money_left_for_tickets = budget * 0.4
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 24:
        money_left_for_tickets = budget * 0.5
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people <= 49:
        money_left_for_tickets = budget * 0.6
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")
    elif number_of_people >= 50:
        money_left_for_tickets = budget * 0.75
        diff = abs(money_left_for_tickets - price_of_tickets)
        if money_left_for_tickets >= price_of_tickets:
            print(f"Yes! You have {diff:.2f} leva left.")
        elif money_left_for_tickets < price_of_tickets:
            print(f"Not enough money! You need {diff:.2f} leva.")


