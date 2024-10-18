text = input()
forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
result = [char for char in text if char.lower() not in forbidden_vowels]
print(*result, sep="")
