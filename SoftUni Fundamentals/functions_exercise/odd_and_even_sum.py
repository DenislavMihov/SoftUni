def sum_of_numbers(n):

    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for j in numbers:
        if j % 2 == 0:
            sum_of_even_digits += j
        else:
            sum_of_odd_digits += j
    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

numbers = input()
numbers = [int(x) for x in str(numbers)]

sum_of_numbers(numbers)