n = int(input())

all_numbers_are_even = True

for i in range(n):
    number = int(input())
    if number % 2 != 0:
        all_numbers_are_even = False
        print(f"{number} is odd!")
        break

if all_numbers_are_even:
    print("All numbers are even.")