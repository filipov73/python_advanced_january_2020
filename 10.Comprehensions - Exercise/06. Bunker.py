bunker = {x: {} for x in input().split(", ")}
number = int(input())
# bunker = {}

for _ in range(number):
    category, item, quantity_and_quality = [x for x in input().split(" - ")]
    quantity, quality = [int(z) for x in quantity_and_quality.split(";") for z in x.split(":") if z.isdigit()]
    if category in bunker:
        # bunker[category] = {item: [quantity, quality]}
        bunker[category].update({item: [quantity, quality]})
    else:
        pass
        # bunker[category] = {item: [quantity, quality]}

count_items = sum([v[0] for key, values in bunker.items() for k, v in values.items()])
sum_quality = sum([v[1] for key, values in bunker.items() for k, v in values.items()])
# sum_items = len([x for key, value in bunker.items() for x in value])
average_quality = sum_quality / len(bunker)
print(f"Count of items: {count_items}")
print(f"Average quality: {average_quality:.2f}")
for key, values in bunker.items():
    items = ", ".join([item for item in values.keys()])
    print(f"{key} -> {items}")
