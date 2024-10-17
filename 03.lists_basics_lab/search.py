n = int(input())
word = input()
special_word = word
strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings = []

for string in strings:
    if special_word in string:
        filtered_strings.append(string)
print(filtered_strings)
