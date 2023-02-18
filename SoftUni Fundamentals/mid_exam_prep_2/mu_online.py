rooms = input().split("|")

bitcoins = 0
MAX_HEALTH = 100
health = MAX_HEALTH
is_alive = True
current_room = 0

for room in rooms:
    command_args = room.split()
    command = command_args[0]
    amount = int(command_args[1])

    if not is_alive:
        break
    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
        current_room += 1
    elif command == "chest":
        bitcoins += amount
        current_room += 1
        print(f"You found {amount} bitcoins.")

    else:
        current_room += 1
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {current_room}")
            is_alive = False

if is_alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")