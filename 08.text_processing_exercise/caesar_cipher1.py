initial_message = input()
encrypted_message = ""
for character in initial_message:
    encrypted_charter = chr(ord(character) + 3)
    encrypted_message += encrypted_charter
print(encrypted_message)
