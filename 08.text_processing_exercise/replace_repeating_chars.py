text = input()
final_text = ""
last_charter = ""
for current_character in text:
    if current_character != last_charter:
        final_text += current_character
        last_charter = current_character
print(final_text)