from collections import deque


def create_base():
    base = deque([])
    count = 0
    for ch in input().split():
        if ch.isdigit():
            base.append(int(ch))
        elif ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count += 1
            base.append(ch)
    return base, count


capacity = int(input())
base, count_halls = create_base()
free_halls = deque([])
rez = []
temp_hall = {}

while True:
    if free_halls and (len(temp_hall) == 0):
        for _ in range(len(free_halls)):
            base.append(free_halls.pop())
    current = base.pop()
    if isinstance(current, str):
        if not temp_hall:
            temp_hall[current] = []
            name = current
        else:
            free_halls.append(current)
    else:
        if temp_hall:
            if sum(temp_hall[name]) + current < capacity:
                temp_hall[name].append(current)
                if len(base) == 0:
                    break
            elif sum(temp_hall[name]) + current == capacity:
                temp_hall[name].append(current)
                temp_hall[name].append(name)
                rez.append(temp_hall[name])
                # print(f"{name} -> {', '.join(map(str, temp_hall[name]))}, {current}")
                del temp_hall[name]
                name = None
            else:
                temp_hall[name].append(name)
                rez.append(temp_hall[name])
                # print(f"{name} -> {', '.join(map(str, temp_hall[name]))}")
                del temp_hall[name]
                name = None
                base.append(current)
        # else:
        #     base.appendleft(current)
    if (len(free_halls) == 0) and (len(temp_hall) == 0) and all([isinstance(x, int) for x in base]):
        break
    if all([isinstance(x, str) for x in base]):
        break
for i in rez:
    name = i.pop()
    r = ", ".join(map(str, i))
    print(f"{name} -> {r}")
