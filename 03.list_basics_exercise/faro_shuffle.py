deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_off_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_off_the_deck]
    right_part = deck_of_cards[middle_off_the_deck::]
    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
        deck_of_cards = final_deck
print(deck_of_cards)
