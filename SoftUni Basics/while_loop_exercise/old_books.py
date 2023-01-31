book = input()

count = 0
input_line = input()
is_found = False
while input_line != "No More Books":
    if book == input_line:
        is_found = True
        break

    count = count + 1
    input_line = input()

if is_found:
    print(f"You checked {count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count} books.")