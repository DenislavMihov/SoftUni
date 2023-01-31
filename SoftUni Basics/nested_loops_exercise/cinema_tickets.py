command = input()

total_sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    if command == "Finish":
        break
    movie_name = command
    empty_seats = int(input())
    sum_of_sold_ticket = 0

    second_command = input()
    while second_command != "End" and second_command != "Finish":
        type_of_ticket = second_command
        sum_of_sold_ticket += 1
        total_sold_tickets += 1
        if type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_tickets += 1
        elif type_of_ticket == "kid":
            kid_tickets += 1




        second_command = input()
    percent_seats = (sum_of_sold_ticket * 100) / empty_seats
    print(f"{movie_name} - {percent_seats}% full.")

    command = input()

percent_student_tickets = (student_tickets * 100) / total_sold_tickets
percent_standard_tickets = (standard_tickets * 100) / total_sold_tickets
percent_kid_tickets = (kid_tickets * 100) / total_sold_tickets

print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% student tickets.")
print(f"{percent_kid_tickets:.2f}% student tickets.")