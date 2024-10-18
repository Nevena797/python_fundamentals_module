vowels = ['a', 'o', 'u', 'e', 'i']
new_text = [el for el in input() if el.lower() not in vowels]
print(''.join(new_text))

