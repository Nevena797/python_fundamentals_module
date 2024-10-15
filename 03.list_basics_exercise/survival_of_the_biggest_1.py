numbers = input().split()  # ['10', '9', '8', '7', '6', '5']
new_numbers = list(map(int, numbers))  # [10, 9, 8, 7, 6, 5]
number_to_remove = int(input())

for i in range(number_to_remove):
    current_min_element = min(new_numbers)
    new_numbers.remove(current_min_element)

print(*new_numbers, sep=", ")
