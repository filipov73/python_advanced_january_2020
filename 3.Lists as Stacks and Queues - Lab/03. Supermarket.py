from collections import deque

name_deque = deque([])
name = input()

while name != "End":
    if name == "Paid":
        print("\n".join(name_deque))
        name_deque.clear()
    else:
        name_deque.append(name)
    name = input()

print(f"{len(name_deque)} people remaining.")
