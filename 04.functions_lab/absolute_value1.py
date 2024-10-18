def sequence_of_numbers(current_numbers):

    print(current_numbers)
    return current_numbers

numbers = [abs(float(num)) for num in input().split()]
sequence_of_numbers(numbers)
