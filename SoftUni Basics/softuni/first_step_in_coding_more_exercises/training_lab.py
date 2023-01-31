#Височина и широчина в метри
w_in_m = float(input())
h_in_m = float(input())

#Височина и широчина в сантиметри
w_in_cm = w_in_m * 100
h_in_cm = h_in_m * 100

hall_in_cm = 100

desk_in_a_row = (h_in_cm - hall_in_cm) // 70

number_of_rows = w_in_cm // 120

number_of_seats = desk_in_a_row * number_of_rows - 3

print(number_of_seats)



