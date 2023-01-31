gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command = command.split()

    if "OutOfStock" in command:

        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"

    elif "Required" in command:
        command_gift = command[1]
        command_index = int(command[2])

        if 0 < command_index < len(gifts) - 1:
            gifts[command_index] = command_gift

    elif "JustInCase" in command:
        command_gift_2 = command[1]
        gifts[-1] = command_gift_2

while "None" in gifts:
    gifts.remove("None")

print(*gifts, sep=" ")


