def smallest_number(some_numbers):
    min_elemet = min(some_numbers)
    return min_elemet


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
smallest_element = smallest_number(numbers)
print(smallest_element)
