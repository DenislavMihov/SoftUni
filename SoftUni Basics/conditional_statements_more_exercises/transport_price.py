number_of_kilomerters = int(input())
day_or_night = input()

taxi_day_price = 0.70 + (0.79 * number_of_kilomerters)
taxi_night_price = 0.70 + (0.9* number_of_kilomerters)
autobuss_price = 0.09 * number_of_kilomerters
train_price = 0.06 * number_of_kilomerters

if number_of_kilomerters < 20:
    if day_or_night == "day":
        print(f"{taxi_day_price:.2f}")
    elif day_or_night == "night":
        print(f"{taxi_night_price:.2f}")
elif number_of_kilomerters < 100:
    print(f"{autobuss_price:.2f}")
elif number_of_kilomerters >= 100:
    print(f"{train_price:.2f}")
