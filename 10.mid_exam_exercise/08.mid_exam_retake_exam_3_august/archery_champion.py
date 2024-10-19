targets = input().split("|")
command = input()

while command != "Game over":
    current_command = command.split(" ")
    if current_command[0] == "Shoot":
        total_command = current_command.split("@")
        direction = current_command

