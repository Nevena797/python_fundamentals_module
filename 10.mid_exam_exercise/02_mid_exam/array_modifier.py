numbers = list(map(int, input().split(" ")))
command = input()
new_list = []

while command != "end":

    if command == "decrease":
        numbers = list(map(lambda n: n - 1, numbers))
    else:
        current_command = command.split(" ")
        command = current_command[0]
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        if current_command[0] == "swap":
            numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
        elif current_command[0] == "multiply":
            numbers[first_index] = numbers[first_index] * numbers[second_index]
    command = input()
numbers = list(map(str, numbers))
new_list = ", ".join(numbers)
print(new_list)
