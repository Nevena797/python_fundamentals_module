from math import ceil
number_of_the_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
maximum_bonus_points = 0
attendances = 0
total_bonus = 0

for attendance in range(number_of_the_students):
    student_attendances = int(input())
    current_bonus = student_attendances / total_number_of_lectures * (5 + additional_bonus)
    if current_bonus > maximum_bonus_points:
        maximum_bonus_points = current_bonus
        attendances = student_attendances

print(f"Max Bonus: {ceil(maximum_bonus_points)}.")
print(f"The student has attended {attendances} lectures.")
