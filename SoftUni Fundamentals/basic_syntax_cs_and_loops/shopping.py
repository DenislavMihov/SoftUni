budget = int(input())

current_price_as_string = input()

while current_price_as_string != "End":
    current_price = int(current_price_as_string)

    budget -= current_price

    if budget < 0:
        print("You went in overdraft!")
        exit()
    current_price_as_string = input()

print("You bought everything needed.")