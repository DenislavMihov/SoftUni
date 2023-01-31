count_jury = int(input())

sum_all_grades = 0
count_all_grades = 0

presentation = input()

while presentation != "Finish":

    sum_grades_per_presentation = 0

    for jury in range(1, count_jury + 1):
        grade = float(input())
        sum_grades_per_presentation += grade
        sum_all_grades += grade
        count_all_grades += 1

    average_grade_per_presentation = sum_grades_per_presentation / count_jury
    print(f"{presentation} - {average_grade_per_presentation:.2f}.")

    presentation = input()

avr_grade = sum_all_grades / count_all_grades

print(f"Student's final assessment is {avr_grade:.2f}.")