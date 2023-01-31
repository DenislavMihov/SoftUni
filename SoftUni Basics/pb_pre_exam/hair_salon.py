target_for_a_day = int(input())
current_target = target_for_a_day

colected_money = 0
flag = False

while True:
    command = input()

    if command == "closed":
        break

    service = command
    kind_of_service = input()

    if service == "haircut":
        if kind_of_service == "mens":
            colected_money += 15
            current_target -= 15
        elif kind_of_service == "ladies":
            colected_money += 20
            current_target -= 20
        elif kind_of_service == "kids":
            colected_money += 10
            current_target -= 10

    elif service == "color":
        if kind_of_service == "touch up":
            colected_money += 20
            current_target -= 20
        elif kind_of_service == "full color":
            colected_money += 30
            current_target -= 30

    if current_target == 0:
        flag = True
        break

diff = abs(target_for_a_day - colected_money)

if flag:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    
print(f"Earned money: {colected_money}lv.")
