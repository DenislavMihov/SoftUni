import sys

command = input()

current_number = sys.maxsize

while command != "Stop":
    num = int(command)

    if num < current_number:
        current_number = num
    else:
        command = input()
        continue
print(current_number)
