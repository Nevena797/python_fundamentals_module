numbers = int(input())

for num in range(1, numbers + 1):
    is_special = False
    sum_digits = 0
    digit = num
    while digit:
        last_num = digit % 10
        sum_digits += last_num
        digit = int(digit / 10) #//10
    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        is_special = True
    print(f"{num} -> {is_special}")
