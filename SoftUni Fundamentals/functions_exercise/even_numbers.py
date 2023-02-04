def my_func(x):
  if x % 2 != 0:
    return False
  else:
    return True

numbers_as_string = input().split()
numbers = []
for num_as_string in numbers_as_string:
    numbers.append(int(num_as_string))

even_numbers_filter = filter(my_func, numbers)
even_numbers = []

for x in even_numbers_filter:
  even_numbers.append(x)

print(even_numbers)