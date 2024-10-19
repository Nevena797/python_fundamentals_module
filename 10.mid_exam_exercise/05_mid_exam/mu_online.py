INITIAL_HEALTH = 100
current_health = 100
initial_bitcoins = 0
best_room = 0
rooms = input().split("|")
dyed = False

for room in rooms:
    action, amount = room.split(" ")
    amount = int(amount)
    best_room += 1
    if action == "potion":
        if action == "potion":
            if current_health + amount > INITIAL_HEALTH:
                print(f"You healed for {INITIAL_HEALTH - current_health} hp.")
                current_health = INITIAL_HEALTH
            else:
                print(f"You healed for {amount} hp.")
                current_health += amount
            print(f"Current health: {current_health} hp.")

    elif action == "chest":
        initial_bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        current_health -= int(amount)
        if current_health <= 0:
            dyed = True
            break
        else:
            print(f"You slayed {action}.")
if dyed:
    print(f"You died! Killed by {action}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {current_health}")
