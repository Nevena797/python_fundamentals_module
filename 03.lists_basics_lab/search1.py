number = int(input())
word = input()
old_list = []
new_list = []

for _ in range(number):
    current_string = input()
    old_list.append(current_string)
    if word in current_string:
        new_list.append(current_string)
print(old_list)
print(new_list)


