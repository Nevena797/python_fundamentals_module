first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
needed_time = 0
total_time = 0
total_students_per_hour = first_employee + second_employee + third_employee

while students_count > 0:
    needed_time += 1
    total_time += 1
    if needed_time % 4 == 0:
        continue
    students_count -= total_students_per_hour
print(f"Time needed: {total_time}h.")
