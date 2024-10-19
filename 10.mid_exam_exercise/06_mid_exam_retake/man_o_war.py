# pirate_ship = [int(num) for num in input().split(">")]
# warship = [int(num) for num in input().split(">")]
#
# max_health_capacity = int(input())
#
# command = input()
#
# while not command == "Retire":
#     data = command.split()
#     if data[0] == "Fire":
#         index = int(data[1])
#         damage = int(data[2])
#         if 0 <= index < len(warship):
#             warship[index] -= damage
#             if warship[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 break
#     elif data[0] == "Defend":
#         start_index = int(data[1])
#         end_index = int(data[2])
#         damage = int(data[3])
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#
#
#     elif data[0] == "Repair":
#         pass
#     elif data[0] == "Status":
#         pass
#
#     command = input()
