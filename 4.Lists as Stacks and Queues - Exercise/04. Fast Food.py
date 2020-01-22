from collections import deque
food = int(input())
deque = deque([int(x) for x in input().split(" ")])
biggest_order = max(deque)
print(biggest_order)

while deque:
    current_order = deque.popleft()
    if food >= current_order:
        food -= current_order
    else:
        deque.appendleft(current_order)
        print(f"Orders left: {' '.join([str(x) for x in deque])}")
        break

if not deque:
    print("Orders complete")
