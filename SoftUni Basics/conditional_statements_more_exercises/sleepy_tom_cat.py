number_of_rest_days = int(input())

#when work - 63 min
#when rest - 127 min

year = 365
tom_needed_playing_time_in_year = 30000
rest_days_play_time = number_of_rest_days * 127
working_days_play_time = (year - number_of_rest_days) * 63
tom_playing_time = rest_days_play_time + working_days_play_time

diff_min = abs(tom_needed_playing_time_in_year - tom_playing_time)
hour = diff_min // 60
minutes = diff_min % 60

if tom_playing_time > tom_needed_playing_time_in_year:
    print("Tom will run away")
    print(f"{hour} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hour} hours and {minutes} minutes less for play")


