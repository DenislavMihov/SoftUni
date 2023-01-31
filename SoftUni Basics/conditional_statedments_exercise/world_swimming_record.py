import math
world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_sec_m = float(input())

all_time_sec = distance_in_meters * time_in_sec_m
delay = math.floor(distance_in_meters / 15) * 12.5
total_time_with_delay = all_time_sec + delay

if world_record_in_seconds <= total_time_with_delay:
    diff = total_time_with_delay - world_record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time_with_delay:.2f} seconds.")
