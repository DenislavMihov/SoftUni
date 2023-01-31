time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

total_minutes = total_time // 60
total_sec = total_time % 60

if total_sec < 10:
    print(f"{total_minutes}:0{total_sec}")
else:
    print(f"{total_minutes}:{total_sec}")

