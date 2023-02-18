from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_attenadnces = 0
max_bonus = 0

for _ in range(students):
    student_attendances = int(input())

    if lectures != 0:
        total_bonus = (student_attendances / lectures) * (5 + additional_bonus)
        max_bonus = max(max_bonus, total_bonus)
        max_attenadnces = max(max_attenadnces, student_attendances)

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attenadnces} lectures.")