def multiply(first, second):
    return first * second


def divide(first, second):
    return first // second


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def calculator(current_command, first, second):

    if command == "multiply":
        result = multiply(first_number, second_number)
    elif command == "divide":
        result = divide(first_number, second_number)
    elif command == "add":
        result = add(first_number, second_number)
    elif command == "subtract":
        result = subtract(first_number, second_number)

    print(result)

command = input()
first_number = int(input())
second_number = int(input())


calculator(command,first_number,second_number )
