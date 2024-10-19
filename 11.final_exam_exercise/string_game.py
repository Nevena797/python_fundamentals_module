decrypted_string = input()
command = input()
current_decrypted_string = ""

while command != "Done":
    current_command = input().split(" ")
    action = current_command[0]
    if action == "Change":
        char = current_command[1]
        replacement = current_command[2]
        current_decrypted_string = decrypted_string.replace(char, replacement)
        print(current_decrypted_string)
    elif action == "Includes":
        substring = current_command[1]
        if substring in current_decrypted_string:
            print("True")
        else:
            print("False")
        print(substring)
    elif action == "End":
        substring = current_command[1]
        if substring == current_decrypted_string:
            print("True")
        else:
            print("False")
    elif action == "Uppercase":
        current_decrypted_string = current_decrypted_string.upper()
        print(current_decrypted_string)
    elif action == "FindIndex":
        index = current_command[1]
        current_index = current_decrypted_string.index(index)
        print(current_index)
    else: # action == "Cut": #//THIS IS MY STRING!//
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        before_substring = current_decrypted_string[start_index:]
        end_string = before_substring[:end_index]
        print(end_string)
    command = input()
