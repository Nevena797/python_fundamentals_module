def min_func(current_numbers):
    return min(current_numbers)


def max_func(current_numbers):
    return max(current_numbers)


def sum_func(current_numbers):
    return sum(current_numbers)


numbers = [int(x) for x in input().split()]
min_number, max_number, sum_numbers = min(numbers), max_func(numbers), sum_func(numbers)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
