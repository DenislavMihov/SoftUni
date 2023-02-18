def find_idx_by_el(seq, el):
    for el_idx in range(len(seq)):
        if seq[el_idx] == el:
            return el_idx

    return -1

shopping_list = [x for x in input().split("!")]

while True:
    line = input()

    if line == "Go Shopping!":
        break

    command_args = line.split()
    command = command_args[0]
    product = command_args[1]

    if command == "Urgent":
        if product not in shopping_list:
            shopping_list.insert(0, product)

    elif command == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)

    elif command == "Correct":
        new_product = command_args[2]
        idx = find_idx_by_el(shopping_list, product)
        if idx == -1:
            continue
        shopping_list[idx] = new_product

    elif command == "Rearrange":
        if product in shopping_list:
            shopping_list.remove(product)
            shopping_list.append(product)

new_list = ", ".join(shopping_list)
print(new_list)