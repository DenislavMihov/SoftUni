to_do_list = [] * 10

command = input()

while command != "End":
    importance, task = command.split("-")
    importance = int()
    index = importance - 1
    to_do_list[index] = task
    command = input()

print([task for task in to_do_list if task != 0])
