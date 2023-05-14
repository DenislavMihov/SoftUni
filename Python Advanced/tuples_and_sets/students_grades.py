from statistics import mean
n = int(input())

student_grades = {}


for _ in range(n):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in student_grades:
        student_grades[name] = []

    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg = mean(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")