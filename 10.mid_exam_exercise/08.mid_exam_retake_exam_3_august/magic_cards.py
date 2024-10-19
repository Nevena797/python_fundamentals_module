original_deck = input().split(":")
final_deck = []
command = input()
while command != "Ready":
    current_command = command.split()

    if current_command[0] == "Add":
        card_name = current_command[1]
        if card_name in original_deck:
            final_deck.apppend(card_name)
        else:
            print("Card not found.")
    elif current_command[0] == "Insert":
        card_name = current_command[1]
        index_card = int(current_command[2])
        if card_name in original_deck and index_card in range(len(final_deck)):
            final_deck.insert(index_card,card_name)
        else:
            print("Error!")
    elif current_command[0] == "Remove":
        card_name = current_command[1]
        if card_name in final_deck:
            final_deck.remove(card_name)
        else:
            print("Card not found.")
    elif current_command[0] == "Swap":
        pass

    elif current_command[0] == "Shuffle":
        pass

        card_index = int()


