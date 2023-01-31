deposit = input()

acc_balance = 0

while deposit != "NoMoreMoney":
    deposit_money = float(deposit)

    if deposit_money < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit_money:.2f}")
        acc_balance += deposit_money

    deposit = input()

print(f"Total: {acc_balance:.2f}")
