init_num = int(input())



sum_numbers = 0

while True:

    new_num = int(input())
    sum_numbers += new_num

    if sum_numbers >= init_num:
        print(sum_numbers)
        break


