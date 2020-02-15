from os import remove
command = input()

while command != "End":
    tocken = command.split("-")
    if tocken[0] == "Create":
        file_name = tocken[1]
        with open(file_name, "w"):
            pass
    elif tocken[0] == "Add":
        file_name = tocken[1]
        content = tocken[2] + "\n"
        with open(file_name, "a") as file:
            file.write(content)
    elif tocken[0] == "Replace":
        file_name = tocken[1]
        old_string = tocken[2]
        new_string = tocken[3]
        try:
            string = open(file_name, "r").read()
            string = string.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(string)
        except FileNotFoundError:
            print("An error occurred")
    elif tocken[0] == "Delete":
        file_name = tocken[1]
        try:
            remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
    command = input()
