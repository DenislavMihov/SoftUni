type_ticket = input()
rows = int(input())
collums = int(input())

all_seats = rows * collums
price = 0

if type_ticket == "Premiere":
    price = 12
elif type_ticket == "Normal":
    price = 7.5
elif type_ticket == "Discount":
    price = 5

total_income = all_seats * price
print(f"{total_income:.2f} leva")
