numbers = [int(s) for s in input().split(", ")]
current_group_of_numbers = 10
while numbers:
    # filtered_list_for_current_group = []
    filtered_list_for_current_group = [number for number in numbers if number <= current_group_of_numbers]
    # for current_number in numbers:
    #     if current_number <= current_group_of_numbers:
    #         filtered_list_for_current_group.append(current_number)
    print(f"Group of {current_group_of_numbers}'s: {filtered_list_for_current_group}")
    current_group_of_numbers += 10
    numbers = [number for number in numbers if number not in filtered_list_for_current_group]
