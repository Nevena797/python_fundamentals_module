from math import ceil

number_of_people = int(input())
capacity_of_the_elevator = int(input())
courses = ceil(number_of_people / capacity_of_the_elevator)

print(courses)