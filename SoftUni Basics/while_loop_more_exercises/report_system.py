expected_money = int(input())

command = input()
sum_money = 0
counter = 0
payments_in_cash = 0
payments_with_card = 0
counter_cash = 0
counter_card = 0



while command != "End":

    price_of_product = int(command)
    counter += 1

    if counter % 2 == 0:

        if price_of_product < 10:
            print("Error in transaction!")


        else:
            print("Product sold!")
            sum_money += price_of_product
            counter_card += 1
            payments_with_card += price_of_product

    else:

        if price_of_product > 100:
            print("Error in transaction!")

        else:
            print("Product sold!")
            sum_money += price_of_product
            counter_cash += 1
            payments_in_cash += price_of_product




    if sum_money >= expected_money:
        print(f"Average CS: {payments_in_cash / counter_cash:.2f}")
        print(f"Average CC: {payments_with_card / counter_card:.2f}")
        break

    command = input()

if command == "End":
    print("Failed to collect required money for charity.")
