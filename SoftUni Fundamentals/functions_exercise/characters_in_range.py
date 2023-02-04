def get_chars_in_range(start, end):
    result = ""
    for num in range(ord(first_char) + 1, ord(second_char)):
        result += f"{chr(num)} "
    return result

first_char = input()
second_char = input()

print(get_chars_in_range(first_char, second_char))