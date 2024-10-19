price = int(input())
number_of_months = int(input())
savings = 0

for month in range(1, number_of_months + 1):
    if month % 2 != 0 and month != 1:
        savings *= 0.84
    if month % 4 == 0:
        savings *= 1.25
    savings += price * 0.25

difference = savings - price

if difference >= 0:
    print(f"Bravo! You can go to Disneyland and you will have {difference:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(difference):.2f}lv. more.")
