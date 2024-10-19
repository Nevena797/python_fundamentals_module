username = input()
data = input()

while data != "Registration":

    splitted_data = data.split(" ")
    command = splitted_data[0]

    if command == "Letters":
        lower_upper = splitted_data[1]
        if lower_upper == "Lower":
            username = username.lower()
        elif lower_upper == "Upper":
            username = username.upper()
        print(username)
    elif command == "Reverse":
        start_index, end_index = int(splitted_data[1]), int(splitted_data[2])
        if 0 <= start_index <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)
    elif command == "Substring":
        current_substring = splitted_data[1]
        if current_substring in username:
            username = username.replace(current_substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {current_substring}.")
    elif command == "Replace":
        char = splitted_data[1]
        if char in username:
            username = username.replace(char, "-")
            print(username)
    elif command == "IsValid":
        current_char = splitted_data[1]
        if current_char in username:
            print(f"Valid username.")
        else:
            print(f"{current_char} must be contained in your username.")
    data = input()

