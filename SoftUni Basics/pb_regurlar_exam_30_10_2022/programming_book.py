price_per_page = float(input())
price_per_cover = float(input())
discount_printing_paper = int(input())
cost_for_disigner = float(input())
percent_team_cost = int(input())

pages = 899
covers = 2

sum_for_printing = (price_per_page * pages) + (price_per_cover * covers)

discount_money = sum_for_printing * discount_printing_paper / 100

cost_plus_designer = sum_for_printing - discount_money + cost_for_disigner

team_cost = (cost_plus_designer * percent_team_cost) / 100

end_cost = cost_plus_designer - team_cost
print(f"Avtonom should pay {end_cost:.2f} BGN.")

