import re
pattern = r"\d+"

strings = input()
list_of_numbers = []

while True:
    if len(strings) == 0:
        break
    numbers = re.findall(pattern, strings)
    list_of_numbers.extend(numbers)
    strings = input()

print(" ".join(list_of_numbers))