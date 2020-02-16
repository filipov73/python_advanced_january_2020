from os import remove

command = input()

while command != "End":
    tokens = command.split('-')
    file_name = tokens[1]
    if tokens[0] == "Create":
        with open(file_name, 'w') as file:
            pass
    elif tokens[0] == "Add":
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif tokens[0] == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        try:
            with open(file_name, 'r') as file:
                file_data = file.read()
            new_data = file_data.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(new_data)

        except FileNotFoundError:
            print('An error occurred')
    elif tokens[0] == "Delete":
        try:
            remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
