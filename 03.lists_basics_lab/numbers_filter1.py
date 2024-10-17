number = int(input())

list_of_even = []
list_of_odd = []
list_of_negative = []
list_of_positive = []

for _ in range(number):
    current_number = int(input())

    if current_number >= 0:
        list_of_positive.append(current_number)
    else:
        list_of_negative.append(current_number)
    if current_number % 2 == 0:
        list_of_even.append(current_number)
    else:
        list_of_odd.append(current_number)


command = input()

if command == "even":
    print(list_of_even)
elif command == "odd":
    print(list_of_odd)
elif command == "negative":
    print(list_of_negative)
else:
    print(list_of_positive)
