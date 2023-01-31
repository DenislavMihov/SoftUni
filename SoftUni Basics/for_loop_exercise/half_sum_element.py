import sys

n = int(input())


max_num = -sys.maxsize

total_sum = 0

for i in range(1, n +1):
    current_number = int(input())

    if current_number > max_num:
        max_num = current_number

    total_sum = total_sum + current_number

other_nums_sum = total_sum - max_num

if other_nums_sum == max_num:
    print("Yes")
    print(f"Sum = {other_nums_sum}")

else:
    print("No")
    diff = abs(other_nums_sum - max_num)
    print(f"Diff = {diff}")

