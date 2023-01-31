n = int(input())


for num in range (1, n +1):
    is_special = False
    if num == 5 or num == 7 or num == 11:
        is_special = True
        print(f"{num} ->")
