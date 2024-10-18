data = input().split()
commands = []

while True:
    command = input()
    if command == "3:1":
        break
    commands.append(command)

for command in commands:
    tokens = command.split()
    action = tokens[0]

    if action == "merge":
        start_index, end_index = int(tokens[1]), int(tokens[2])
        start_index = max(0, start_index)
        end_index = min(end_index, len(data) - 1)
        merged = "".join(data[start_index:end_index + 1])
        data = data[:start_index] + [merged] + data[end_index + 1:]

    elif action == "divide":
        index, partitions = int(tokens[1]), int(tokens[2])
        substring = data[index]
        partition_size = len(substring) // partitions
        extra = len(substring) % partitions
        divided_substrings = []

        for i in range(partitions):
            if i < extra:
                divided_substrings.append(substring[i * (partition_size + 1):(i + 1) * (partition_size + 1)])
            else:
                divided_substrings.append(substring[i * partition_size:(i + 1) * partition_size])

        data = data[:index] + divided_substrings + data[index + 1:]

print(" ".join(data))