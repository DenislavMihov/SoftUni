def check_for_perf_number(n):
    check_number = 0
    for i in range(1, n):
        if n % i == 0:
            check_number = check_number + i
    if check_number == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())

print(check_for_perf_number(number))
