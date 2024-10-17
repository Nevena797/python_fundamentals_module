def odd_even_sum(current_number):
    sum_odd_digits = 0
    sum_even_digits = 0
    for num1 in current_number:
        if int(num1) % 2 == 0:
            sum_even_digits += int(num1)
        else:
            sum_odd_digits += int(num1)
    return sum_odd_digits, sum_even_digits


number = input()
sum_odd_digits, sum_even_digits = odd_even_sum(number)
print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")
