lenght_of_cake = int(input())
width_of_cake = int(input())

size_of_cake = lenght_of_cake * width_of_cake


command = input()

while True:
    if command != "STOP":
        pieces = int(command)
        size_of_cake -= pieces

        if size_of_cake <= 0:
            print(f"No more cake left! You need {abs(size_of_cake)} pieces more.")
            break

        else:
            command = input()
            continue
    else:
        print(f"{size_of_cake} pieces are left.")
        break
        