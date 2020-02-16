from os import remove

while True:
    line = input().split('-')
    command = line[0]

    if command == 'End':
        break

    elif command == 'Create':
        name = line[1]
        with open(name, 'w') as file:
            pass

    elif command == 'Add':
        name, content = line[1], line[2]
        with open(name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        name, old_str, new_str = line[1], line[2], line[3]
        try:
            with open(name, 'r') as file:
                data = file.read()
                new_data = data.replace(old_str, new_str)

            with open(name, 'w') as file:
                file.write(new_data)

        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        name = line[1]
        try:
            remove(name)
        except FileNotFoundError:
            print('An error occurred')
