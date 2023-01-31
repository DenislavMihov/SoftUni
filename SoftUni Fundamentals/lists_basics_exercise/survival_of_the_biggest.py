numbers_as_string = input().split()

numbers_as_digits = []

for element in numbers_as_string:
    numbers_as_digits.append(int(element))

count_of_numbers_to_remove = int(input())

for _ in range(count_of_numbers_to_remove):
    numbers_as_digits.remove(min(numbers_as_digits))

print(*numbers_as_digits, sep=", ")
