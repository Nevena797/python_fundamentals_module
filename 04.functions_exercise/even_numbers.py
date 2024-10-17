def even_numbers(current_numbers):
    list_even_numbers = []
    for number in current_numbers:
        if int(number) % 2 == 0:
            list_even_numbers.append(int(number))
    return list_even_numbers


numbers = input().split()
list_even_numbers = even_numbers(numbers)
print(list_even_numbers)
