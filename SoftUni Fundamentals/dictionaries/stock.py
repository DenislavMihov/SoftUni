products = {}

data = input().split()
searched_products = input().split()

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index+1])
    products[key] = value



for searched_product in searched_products:
    if searched_product in products.keys():
        quantity = products[searched_product]
        print(f"We have {quantity} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")
