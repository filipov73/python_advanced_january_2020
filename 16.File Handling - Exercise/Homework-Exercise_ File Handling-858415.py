from os import remove

line = input().split('-')
while line[0] != "End":
    command = line[0]
    file_name = line[1]
    if command == "End":
        break
    elif command == "Create":
        with open(file_name, 'w') as f:
            pass
    elif command == "Add":
        to_add = line[2]
        with open(file_name, 'a') as f:
            f.write(f"{to_add}\n")
    elif command == "Replace":
        to_be_replaced = line[2]
        to_replace_with = line[3]
        try:
            with open(file_name, 'r') as f:
                file_data = f.read()
                new_data = file_data.replace(to_be_replaced, to_replace_with)
            with open(file_name, 'w') as f:
                f.write(new_data)
        except FileNotFoundError:
            print('An error occurred')
    elif command == "Delete":
        try:
            remove(file_name)
        except FileNotFoundError:
            print('An error occurred')
    line = input().split('-')