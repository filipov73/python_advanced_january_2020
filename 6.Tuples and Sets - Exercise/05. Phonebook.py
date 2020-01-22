def read_until_command(end_command):
    dict_ = {}
    while True:
        command = input()
        if command == end_command:
            return dict_
        name, tel = command.split("-")

        if name not in dict_:
            dict_[name] = ""
        dict_[name] = tel


dict_ = read_until_command("search")

while True:
    search_name = input()
    if search_name == "stop":
        break
    if search_name in dict_:
        print(f"{search_name} -> {dict_[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
