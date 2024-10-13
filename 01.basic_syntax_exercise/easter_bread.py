budget = float(input())
one_kg_flour_price = float(input())
current_bread_count = 0
colored_eggs_counter = 0
eggs_price = one_kg_flour_price * 0.75
milk_price = one_kg_flour_price * 1.25 / 4

price_one_bread = one_kg_flour_price + eggs_price + milk_price
while budget > price_one_bread:
    budget -= price_one_bread
    current_bread_count += 1
    colored_eggs_counter += 3
    if current_bread_count % 3 == 0:
        colored_eggs_counter -= current_bread_count - 2
print(
    f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
