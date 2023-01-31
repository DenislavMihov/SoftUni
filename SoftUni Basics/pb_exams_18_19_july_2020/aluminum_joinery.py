number_of_joinery = int(input())
type_of_joinery = input()
shipment_method = input()

sum_of_order = 0



if number_of_joinery > 10:

    if type_of_joinery == "90X130":
        if number_of_joinery <= 30:
            sum_of_order = 110 * number_of_joinery

        elif number_of_joinery <= 60:
            sum_of_order = (110 * number_of_joinery) * 0.95

        else:
            sum_of_order = (110 * number_of_joinery) * 0.92

    elif type_of_joinery == "100X150":
        if number_of_joinery <= 40:
            sum_of_order = 140 * number_of_joinery

        elif number_of_joinery <= 80:
            sum_of_order = (140 * number_of_joinery) * 0.94

        else:
            sum_of_order = (140 * number_of_joinery) * 0.90

    elif type_of_joinery == "130X180":
        if number_of_joinery <= 20:
            sum_of_order = 190 * number_of_joinery

        elif number_of_joinery <= 50:
            sum_of_order = (190 * number_of_joinery) * 0.93

        else:
            sum_of_order = (190 * number_of_joinery) * 0.88

    elif type_of_joinery == "200X300":
        if number_of_joinery <= 25:
            sum_of_order = 250 * number_of_joinery

        elif number_of_joinery <= 50:
            sum_of_order = (250 * number_of_joinery) * 0.91

        else:
            sum_of_order = (250 * number_of_joinery) * 0.86

if shipment_method == "With delivery" and number_of_joinery > 10:
    sum_of_order += 60

if number_of_joinery > 99:
    sum_of_order = sum_of_order * 0.96

if number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{sum_of_order:.2f} BGN")
