neighborhood = [int(num) for num in input().split("@")]

command = input()
position = 0

while not command == "Love!":
    length_jump = command.split()[1]
    length_jump = int(length_jump)

    position = position + length_jump

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had "
              f"Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

houses_with_v_day = neighborhood.count(0)

if houses_with_v_day == len(neighborhood):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood)-houses_with_v_day} places.")
