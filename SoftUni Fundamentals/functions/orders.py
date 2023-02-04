def price_of_order(product, quantity):

    result = 0

    if product == "coffee":
        result = 1.50 * quantity
    if product == "water":
        result = 1.00 * quantity
    if product == "coke":
        result = 1.40 * quantity
    if product == "snacks":
        result = 2.00 * quantity

    return result

product = input()
quantity = float(input())

res = price_of_order(product, quantity)

print(f"{res:.2f}")