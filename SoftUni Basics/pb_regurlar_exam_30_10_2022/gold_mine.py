num_locations = int(input())

for location in range(num_locations):
    expected_average = float(input())
    num_of_days = int(input())
    total_mined_gold = 0

    for days in range(num_of_days):
        mined_gold = int(input())
        total_mined_gold += mined_gold

    average_mined_gold = total_mined_gold / num_of_days
    diff = abs(expected_average - average_mined_gold)

    if average_mined_gold >= expected_average:
        print(f"Good job! Average gold per day: {average_mined_gold:.2f}.")

    elif average_mined_gold < expected_average:
        print(f"You need {diff:.2f} gold.")
