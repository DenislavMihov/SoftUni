kids = 0
adults = 0

while True:
    age = input()
    if age != "Christmas":
        age = int(age)

        if age > 16:
            adults += 1
        else:
            kids += 1

    if age == "Christmas":
        break

price_toys = kids * 5
price_jumpers = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {price_toys}")
print(f"Money for sweaters: {price_jumpers}")
