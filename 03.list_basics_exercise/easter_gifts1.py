#
# 70%
#
# def out_of_stock(gifts, current_gift):
#     for idx in range(len(gifts)):
#         if gifts[idx] == current_gift:
#             gifts[idx] = "None"
#     return gifts
#
#
# def required(gifts, replaced_gift, current_index):
#     if 0 <= current_index < len(gifts):
#         gifts[current_index] = replaced_gift
#     return gifts
#
#
# def just_in_case(gifts, replaced_gift):
#     gifts[-1] = replaced_gift
#     return gifts
#
#
# gifts = input().split()  # ['Eggs', 'StuffedAnimal', 'Cozonac', 'Sweets', 'EasterBunny', 'Eggs', 'Clothes']
#
# line = input()
#
# while line != "No Money":
#
#     current_command = line.split()
#     command = current_command[0]
#     gift = current_command[1]
#     if command == "OutOfStock":
#         gifts = out_of_stock(gifts, gift)
#     elif command == "Required":
#         index = int(current_command[2])
#         gifts = required(gifts, gift, index)
#     elif command == "JustInCase":
#         gifts = just_in_case(gifts, gift)
#     line = input()
#
# for gift in gifts:
#     if gift == "None":
#         gifts.remove(gift)
# print(*gifts, end=' ')
