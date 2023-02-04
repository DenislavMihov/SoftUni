numbers_as_string = input().split()
numbers_as_digits = []

for num_as_string in numbers_as_string:
    numbers_as_digits.append(int(num_as_string))

sorted_numbers = sorted(numbers_as_digits)

print(sorted_numbers)