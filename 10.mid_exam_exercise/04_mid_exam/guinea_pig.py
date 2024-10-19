food_in_kilograms = float(input())
hay_in_kilograms = float(input())
cover_in_kilograms = float(input())
guinea_weight = float(input())

food_in_grams = food_in_kilograms * 1000
hay_in_grams = hay_in_kilograms * 1000
cover_in_grams = cover_in_kilograms * 1000
weight_in_grams = guinea_weight * 1000
go_to_the_store = False


for day in range(1, 31):
    food_in_grams -= 300
    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0:
        cover_in_grams -= weight_in_grams / 3
    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        go_to_the_store = True
        break

if not go_to_the_store:
    food, hay, cover = food_in_grams / 1000, hay_in_grams / 1000, cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, "
          f"Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(f"Merry must go to the pet store!")
