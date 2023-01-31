nylon_per_sq_mt = 1.50
paint_per_lt = 14.50
paint_thinner_per_lt = 5.00
bags = 0.40

needed_nylon_in_sq_mt = int(input())
needed_paint_in_lt = int(input())
needed_paint_thinner_in_lt = int(input())
numer_of_hours = int(input())

nylon_sum = (needed_nylon_in_sq_mt + 2) * 1.5
paint_sum = (needed_paint_in_lt * 1.1) * paint_per_lt
thinner_sum = needed_paint_thinner_in_lt * paint_thinner_per_lt

matirials_total_sum = bags + nylon_sum + paint_sum + thinner_sum

craftsman_cost_per_hour = matirials_total_sum * 0.3
craftsman_total_cost = craftsman_cost_per_hour * numer_of_hours

end_cost = matirials_total_sum + craftsman_total_cost

print(f"{end_cost}")




