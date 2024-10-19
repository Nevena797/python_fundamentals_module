def change(current_decrypted_string, command):
    char = current_command[1]
    replacement = current_command[2]
    current_decrypted_string = decrypted_string.replace(char, replacement)
    return current_decrypted_string


def includes(current_decrypted_string, command):
    substring = current_command[1]
    if substring in current_decrypted_string:
        substring = True
    else:
        substring = False
    return current_decrypted_string

def end(current_decrypted_string, command):
    substring = current_command[1]
    if substring == current_decrypted_string:
        print("True")
    else:
        print("False")
    return current_decrypted_string

def uppercase(current_decrypted_string, command):
    current_decrypted_string = current_decrypted_string.upper()
    return current_decrypted_string


def find_index(current_decrypted_string, command):
    index = current_command[1]
    current_index = current_decrypted_string.index(index)
    return current_decrypted_string

def cut(current_decrypted_string, command):
    start_index = current_command[1]
    end_index = current_command[2]
    before_substring = current_decrypted_string[:start_index]
    after_substring = current_decrypted_string[end_index:]
    current_decrypted_string = before_substring + after_substring
    return current_decrypted_string


decrypted_string = input()

while True:
    current_command = input()
    if current_command == "Done":
        break
    current_command = input().split(" ")
    action = current_command[0]
    if action == "Change":
        decrypted_string = change(decrypted_string, current_command)
        print(change(decrypted_string, current_command))
    elif action == "Includes":
        decrypted_string = change(decrypted_string, current_command)
        print(decrypted_string)
    elif action == "End":
        decrypted_string = end(decrypted_string, current_command)
        print(decrypted_string)
    elif action == "Uppercase":
        decrypted_string = end(decrypted_string, current_command)
        print(uppercase)
    elif action == "FindIndex":
        decrypted_string = find_index(decrypted_string, current_command)
        print(find_index(decrypted_string, current_command))
    elif action == "Cut":
        decrypted_string = cut(decrypted_string, current_command)
        print(cut(decrypted_string, current_command))