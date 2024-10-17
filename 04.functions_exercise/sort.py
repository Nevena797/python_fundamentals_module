def sorted_funk(numbers):
    return sorted(numbers)


sequence_of_numbers = list(map(int, input().split()))
sorted_numbers = sorted_funk(sequence_of_numbers)
print(sorted_numbers)
