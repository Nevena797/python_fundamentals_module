factor = int(input())
count = int(input())
list_of_numbers = []

for i in range(1, count + 1):
    new_number = i * factor
    list_of_numbers.append(new_number)
print(list_of_numbers)
