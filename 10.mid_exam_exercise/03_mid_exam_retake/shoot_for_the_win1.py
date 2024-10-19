targets = list(map(int, input().split()))

shoots = 0

while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    if index >= len(targets):
        continue
    last_shoot = 0
    if targets[index] != -1:
        last_shoot = targets[index]
        targets[index] = -1
        shoots += 1
    for num in range(len(targets)):
        if targets[num] != -1:
            if targets[num] > last_shoot:
                targets[num] -= last_shoot
            else:
                targets[num] += last_shoot

print(f'Shot targets: {shoots} ->', *targets)