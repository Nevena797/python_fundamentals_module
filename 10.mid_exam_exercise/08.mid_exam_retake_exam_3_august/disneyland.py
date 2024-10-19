price = int(input())
number_of_months = int(input())
savings = 0

for month in range(number_of_months):
    if month % 2 != 0:
        if month != 1:
            savings -= savings * 0.16
    if month % 4 == 0:
        if month == 0:
            savings = savings * 0.25

    savings += price * 0.25

difference = price - savings

if savings > price:
    print(f"Bravo! You can go to Disneyland and you will have {abs(difference):.2f}lv. for souvenirs.")

else:
    print(f"Sorry. You need {difference:.2f}lv. more.")
