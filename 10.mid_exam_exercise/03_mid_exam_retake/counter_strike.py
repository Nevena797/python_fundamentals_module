initial_energy = int(input())
count_of_won_battles = 0
total_energy = initial_energy
not_enough_energy = False
distance = input()

while distance != "End of battle":

    current_distance = int(distance)
    if current_distance > total_energy:
        not_enough_energy = True
        break
    else:
        total_energy -= current_distance
        count_of_won_battles += 1
        if count_of_won_battles % 3 == 0:
            total_energy += count_of_won_battles
    distance = input()

if not_enough_energy:
    print(f"Not enough energy! Game ends with {count_of_won_battles} won battles and {total_energy} energy")
else:
    print(f"Won battles: {count_of_won_battles}. Energy left: {total_energy}")
