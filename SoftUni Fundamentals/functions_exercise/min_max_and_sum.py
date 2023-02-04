numbers_as_string = input().split()
numbers_as_digits = []

for num in numbers_as_string:
    numbers_as_digits.append(int(num))

min_num = min(numbers_as_digits)
max_num = max(numbers_as_digits)
sum_num = sum(numbers_as_digits)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")
