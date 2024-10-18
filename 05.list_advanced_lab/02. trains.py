number_of_wagons = int(input())

train = [0] * number_of_wagons
command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
        n_people = int(command.split()[1])
        train[-1] += n_people
    elif action == "insert":
        n_index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[n_index] += n_people
    elif action == "leave":
        n_index = int(command.split()[1])
        n_people = int(command.split()[2])
        train[n_index] -= n_people
    command = input()

print(train)
