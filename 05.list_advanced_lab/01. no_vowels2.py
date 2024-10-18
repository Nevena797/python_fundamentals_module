def no_vowels(current_text):
    forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
    result = [char for char in current_text if char.lower() not in forbidden_vowels]
    return "".join(result)


text = input()
print(no_vowels(text))
