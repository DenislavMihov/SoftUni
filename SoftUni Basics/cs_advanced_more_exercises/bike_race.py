juniors_bikers = int(input())
seniors_bikers = int(input())
route_type = input()
total_bikers = juniors_bikers + seniors_bikers

if route_type == "trail":
    tax_for_juniors = 5.5
    tax_for_seniors = 7
    total_sum_of_taxes = (juniors_bikers * tax_for_juniors) + (seniors_bikers * tax_for_seniors)
    expenses = total_sum_of_taxes * 0.05
    money_left = total_sum_of_taxes - expenses
    print(f"{money_left:.2f}")

elif route_type == "cross-country":
    if total_bikers < 50:
     tax_for_juniors = 8
     tax_for_seniors = 9.5
     total_sum_of_taxes = (juniors_bikers * tax_for_juniors) + (seniors_bikers * tax_for_seniors)
     expenses = total_sum_of_taxes * 0.05
     money_left = total_sum_of_taxes - expenses
     print(f"{money_left:.2f}")

    elif total_bikers >= 50:
     tax_for_juniors = 8
     tax_for_seniors = 9.5
     total_sum_of_taxes = ((juniors_bikers * tax_for_juniors) + (seniors_bikers * tax_for_seniors)) * 0.75
     expenses = total_sum_of_taxes * 0.05
     money_left = total_sum_of_taxes - expenses
     print(f"{money_left:.2f}")

elif route_type == "downhill":
    tax_for_juniors = 12.25
    tax_for_seniors = 13.75
    total_sum_of_taxes = (juniors_bikers * tax_for_juniors) + (seniors_bikers * tax_for_seniors)
    expenses = total_sum_of_taxes * 0.05
    money_left = total_sum_of_taxes - expenses
    print(f"{money_left:.2f}")

elif route_type == "road":
    tax_for_juniors = 20
    tax_for_seniors = 21.5
    total_sum_of_taxes = (juniors_bikers * tax_for_juniors) + (seniors_bikers * tax_for_seniors)
    expenses = total_sum_of_taxes * 0.05
    money_left = total_sum_of_taxes - expenses
    print(f"{money_left:.2f}")
