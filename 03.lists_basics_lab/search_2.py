number = int(input())
word = input()
items = []

for _ in range(number):
    item = input()
    items.append(item)
print(items)

for i in range(len(items) - 1, -1, -1):
    element = items[i]
    if word not in element:
        items.remove(element)
print(items)
