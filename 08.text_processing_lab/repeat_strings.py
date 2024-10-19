data = input().split()
new_tex = [text * len(text) for text in data]

print("".join(new_tex))