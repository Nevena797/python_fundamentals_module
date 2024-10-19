shop = {}
all_sold = 0

while True:
    command = input()
    if command == "Complete":
        for food, quantity in shop.items():
            print(food + ": " + str(quantity))

        print(f"All sold: {all_sold} goods")
        break

    current_command, quantity, food = command.split()
    quantity = int(quantity)

    if current_command == "Receive":
        if quantity <= 0:
            continue

        if food not in shop:
            shop[food] = 0

        shop[food] += quantity

    elif current_command == "Sell":
        if food not in shop:
            print(f"You do not have any {food}.")

        elif quantity > shop[food]:
            all_sold += shop[food]
            print(f"There aren't enough {food}. You sold the last {shop[food]} of them.")
            del shop[food]

        else:
            shop[food] -= quantity
            all_sold = quantity
            print(f"You sold {quantity} {food}.")
            if not shop[food]:
                del shop[food]
