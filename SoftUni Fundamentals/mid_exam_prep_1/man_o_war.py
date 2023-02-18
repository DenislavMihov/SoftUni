def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)

pirates_ship= [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

#12>13>11>20>66
#12>22>33>44>55>32>18
#70
is_running = True


while is_running :
    line = input()
    if line == "Retire":
        break

    command_arg = line.split()
    command = command_arg[0]

    if command == "Fire":
        idx = int(command_arg[1])
        damage = int(command_arg[2])
        if not is_valid_idx(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")


    elif command == "Defend":
        start_idx = int(command_arg[1])
        end_idx = int(command_arg[2])
        damage = int(command_arg[3])
        if not is_valid_idx(start_idx, pirates_ship) or not is_valid_idx(end_idx, pirates_ship):
            continue
        for idx in range(start_idx, end_idx +1):

            pirates_ship[idx] -= damage

            if pirates_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break
    elif command == "Repair":
        idx = int(command_arg[1])
        health = int(command_arg[2])
        if not is_valid_idx(idx, pirates_ship):
            continue
        pirates_ship[idx] = min(max_health, pirates_ship[idx] + health)


    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirates_ship:
            if section < threshold:
                counter += 1
        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirates_ship)}")
    print(f"Warship status: {sum(warship)}")