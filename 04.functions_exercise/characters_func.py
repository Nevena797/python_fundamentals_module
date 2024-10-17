def charters_range(first, second):
    result = " "
    for num in range(ord(first) + 1, ord(second)):
        result += f"{chr(num)} "
    return result


first_char = input()
second_char = input()
print(charters_range(first_char, second_char), end=" ")
