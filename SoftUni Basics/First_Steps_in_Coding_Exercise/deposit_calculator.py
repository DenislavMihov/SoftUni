deposit_money = float(input())
number_of_months = int(input())
interest_rate = float(input())

money_at_the_end = deposit_money + number_of_months * ((deposit_money * interest_rate) / 12)

print(money_at_the_end)
