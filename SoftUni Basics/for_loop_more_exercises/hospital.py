period = int(input())


number_of_doctors = 7
daily_treated_patients = 0
daily_untreated_patients = 0
patients = 0
total_treated_patients = 0
total_untreated_patients = 0
counter = 0

for i in range(1, period + 1):
    patients = int(input())
    if i % 3 == 0 and total_untreated_patients > total_treated_patients:
        number_of_doctors += 1
    if number_of_doctors >= patients:
        daily_treated_patients = patients
        total_treated_patients += daily_treated_patients
        total_untreated_patients += 0

    elif number_of_doctors < patients:
        daily_treated_patients = number_of_doctors
        daily_untreated_patients = patients - number_of_doctors

        total_treated_patients += daily_treated_patients
        total_untreated_patients += daily_untreated_patients


print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")


