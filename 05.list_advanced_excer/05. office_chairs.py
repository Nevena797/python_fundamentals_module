number_of_rooms = int(input())

total_free_chairs = 0
total_needed_chairs = 0

for number_of_room in range(1, number_of_rooms + 1):
    data = input().split()
    current_chairs = len(data[0])
    current_people = int(data[1])

    difference = current_chairs - current_people
    if difference >= 0:
        total_free_chairs += difference
    else:
        total_needed_chairs += abs(difference)
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")

if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

