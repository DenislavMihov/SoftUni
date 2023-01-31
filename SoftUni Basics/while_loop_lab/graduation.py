student_name = input()

sum_grades = 0
current_grade = 0
failed_grades_counter = 0


while True:
    grade = float(input())
    current_grade += 1

    if grade < 4:
        failed_grades_counter += 1
        if failed_grades_counter == 2:
            print(f"{student_name} has been excluded at {current_grade} grade")
            break

        current_grade -= 1

    else:
        sum_grades += grade

    if current_grade == 12:
        average_grade = sum_grades / current_grade
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break






