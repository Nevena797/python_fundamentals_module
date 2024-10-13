divisor = int(input())
boundary = int(input())
for number in range(boundary, divisor - 1, -1):
    #divisor -1, becouse of including divisor
    if number % divisor == 0:
        break
print(number)
