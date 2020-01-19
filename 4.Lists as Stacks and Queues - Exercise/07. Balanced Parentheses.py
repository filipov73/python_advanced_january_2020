from collections import deque




string = [x for x in input()]
new_list = deque([])
parenthesis = {
    "{": 1,
    "[": 2,
    "(": 3,
    ")": 13,
    "]": 12,
    "}": 11,
    " ": 0
}

for ch in string:
    new_list.append(parenthesis[ch])

if len(new_list) % 2 != 0:
    print("NO")
else:
    while new_list:
        first = new_list.popleft()
        last = new_list.pop()
        if first != last - 10:
            print("NO")
            break
        else:
            if not new_list:
                print("YES")
                break


