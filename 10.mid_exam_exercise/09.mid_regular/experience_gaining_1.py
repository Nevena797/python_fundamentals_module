# wanted_experience = int(input())
# count_of_battles = int(input())
# experience_earned_per_battle = int(input())
# current_battle_count = 0
# current_experience = 0
#
# for current_battle_count in range(0, count_of_battles + 1):
#     if current_experience >= wanted_experience:
#         current_battle_count += 1
#         current_experience = experience_earned_per_battle
#     print(f"Player successfully collected his needed experience for {current_battle_count} battles.")
#     exit(0)
#     elif current_experience >= wanted_experience:
#         experience_earned_per_battle = int(input())
#         if current_battle_count % 3 == 0:
#             current_battle_count += 1
#             current_experience += experience_earned_per_battle
#             total_experience = current_experience + (current_experience * 0.15)
#             difference = abs(wanted_experience - total_experience)
#             print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
#         if current_battle_count % 5 == 0:
#             current_battle_count += 1
#             current_experience += experience_earned_per_battle
#             total_experience = current_experience - (current_experience * 0.10)
#             difference = abs(wanted_experience - total_experience)
#             print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
#         if current_battle_count % 15 == 0:
#             current_battle_count += 1
#             current_experience += experience_earned_per_battle
#             total_experience = current_experience + (current_experience * 0.05)
#             difference = abs(wanted_experience - total_experience)
#             print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
