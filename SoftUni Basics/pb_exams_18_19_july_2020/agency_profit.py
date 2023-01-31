name_company = input()
number_of_adult_tickets = int(input())
number_of_child_tickets = int(input())
price_of_adult_ticket = float(input())
tax = float(input())

price_of_child_ticket = price_of_adult_ticket * 0.3

adult_ticket_tax = price_of_adult_ticket + tax
child_ticket_tax = price_of_child_ticket + tax

total_sum_tickets = (number_of_adult_tickets * adult_ticket_tax) + (number_of_child_tickets * child_ticket_tax)
profit_of_agency = 0.2 * total_sum_tickets

print(f"The profit of your agency from {name_company} tickets is {profit_of_agency:.2f} lv.")