import math
number_of_magnolii = int(input())
number_of_zumbuli = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
gift_price = float(input())

# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева

sum = (number_of_magnolii * 3.25) + (number_of_zumbuli * 4) + (number_of_roses * 3.50) + (number_of_cactuses * 8)
taxes = sum * 0.05
profit = sum - taxes
diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {math.floor(diff)} leva.")
elif profit < gift_price:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
