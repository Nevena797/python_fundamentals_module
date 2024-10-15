money = input().split(", ")  # ['1', '2', '3', '4', '5']

new_list = []  # [1, 2, 3, 4, 5]

for element in money:
    new_list.append(int(element))

number_of_beggars = int(input())
total_sum_beggars = []
starting_index = 0

while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money), number_of_beggars):
        sum_for_current_beggar += new_list[current_index]
    total_sum_beggars.append(sum_for_current_beggar)
    starting_index += 1
print(total_sum_beggars)
