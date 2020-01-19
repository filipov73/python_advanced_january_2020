food_quantity = int(input())
orders = list(map(int, input().split(" ")))
orders_left = []
print(max(orders))
for idx in range(len(orders)):
    if food_quantity >= orders[idx]:
        food_quantity -= orders[idx]
    else:
        orders_left.append(orders[idx])
if orders_left:
    print("Orders left: ", end="")
    print(" ".join(map(str, orders_left)))
else:
    print("Orders complete")
