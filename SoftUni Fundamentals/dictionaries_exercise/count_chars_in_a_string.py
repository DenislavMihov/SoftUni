text = input()
counts_of_chars = {}

for char in text:
    if char != " ":
        if char in counts_of_chars:
            counts_of_chars[char] += 1
        else:
            counts_of_chars[char] = 1

for char, count in counts_of_chars.items():
    print(f"{char} -> {count}")

