#Monday
#Tuesday
#Wednesday
#Thursday
#Friday
#Saturday
#Sunday

current_hour = int(input())
day_of_week = input()

if day_of_week in ["Monday", "Tuesday",
                   "Wednesday", "Thursday",
                   "Friday", "Saturday", ]:
  if  10 <= current_hour <= 18:
      print("open")
  else:
      print("closed")

else:
    print("closed")




