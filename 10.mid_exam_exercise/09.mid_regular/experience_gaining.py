wanted_experience = int(input())
count_of_battles = int(input())
experience_earned_per_battle = int(input())
current_battle_count = 0
current_experience = 0
total_experience = 0

while current_battle_count in range(count_of_battles):
    current_battle_count += 1
    current_experience += experience_earned_per_battle
    if count_of_battles % 3 == 0:
        current_experience *= 1.15
    if count_of_battles % 5 == 0:
        current_experience *= 0.95
    if count_of_battles % 15 == 0:
        current_experience *= 1.05
    difference = abs(wanted_experience - current_experience)
    print(f"Player was not able to collect the needed experience, {difference} more needed.")
    break
print(f"Player successfully collected his needed experience for {current_battle_count} battles.")

