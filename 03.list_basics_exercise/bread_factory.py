events = input().split("|")  # ['rest-2', 'order-10', 'eggs-100', 'rest-10 ']
total_energy = 100
total_coins = 100
factory_is_open = True
gained_energy = 0

for event in events:
    event_items = event.split("-")  # rest-2 order-10 eggs-100 rest-10
    event_name = event_items[0]
    event_value = int(event_items[1])
    if event_name == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_name == "order":
        if total_energy >= 30:
            print(f"You earned {event_value} coins.")
            total_energy -= 30
            total_coins += event_value
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_name}.")
        else:
            factory_is_open = False
            break

if factory_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {event_name}.")
