from collections import deque


def check_in_cocktail_dict(cocktail_value, cocktails_dict):
    for key, value in cocktails_dict.items():
        if cocktail_value == value:
            return key


ingredients = deque([int(x) for x in input().split()])
freshness = [int(x) for x in input().split()]

cocktails = {
    "Mimosa": 150,
    "Daiquiri": 250,
    "Sunshine": 300,
    "Mojito": 400,
}

ready_cocktails = {}

while ingredients and freshness:
    current_ingredient = ingredients.popleft()
    current_freshness = freshness.pop()
    if current_ingredient == 0:
        freshness.append(current_freshness)
        continue
    # elif current_freshness == 0:
    #     ingredients.appendleft(current_ingredient)
    #     continue
    cocktail = current_ingredient * current_freshness
    current_cocktail = check_in_cocktail_dict(cocktail, cocktails)
    if current_cocktail:
        if current_cocktail not in ready_cocktails:
            ready_cocktails[current_cocktail] = 0
        ready_cocktails[current_cocktail] += 1
    elif not current_cocktail:
        ingredients.append(current_ingredient + 5)

if len(ready_cocktails) == len(cocktails):
    print("It's party time! The cocktails are ready!")
else:
    print("What a pity! You didn't manage to prepare all cocktails.")

if ingredients:
    print(f"Ingredients left: {sum(ingredients)}")

for key, value in sorted(ready_cocktails.items()):
    print(f"# {key} --> {value}")
