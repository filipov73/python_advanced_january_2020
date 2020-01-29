name = input().split(", ")

hero_dict = {key: [] for key in name}
hero_items_dict = {key: [] for key in name}

command = input()

while command != "End":
    (name, item, cost) = command.split("-")
    if name in hero_dict:
        if item not in hero_items_dict[name]:
            hero_dict[name].append({item: cost})
            hero_items_dict[name].append(item)
    command = input()

for key, value in hero_dict.items():
    sums = sum([int(v) for el in value for k, v in el.items()])
    print(f"{key} -> Items: {len(value)}, Cost: {sums}")
