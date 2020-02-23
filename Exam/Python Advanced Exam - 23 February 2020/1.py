from collections import deque
from math import floor
def evaluator(rez, com):
    rez = deque(rez)
    result = 0
    t = 0
    if com == "+":
        result = rez.popleft()
        for _ in range(len(rez)):
            result += rez.popleft()
    elif com == "-":
        result = rez.popleft()
        for _ in range(len(rez)):
            result -= rez.popleft()

    elif com == "*":
        result = rez.popleft()
        for _ in range(len(rez)):
            result *= rez.popleft()
    elif com == "/":
        result = rez.popleft()
        for _ in range(len(rez)):
            result /= rez.popleft()
        result = floor(result)

    return result


string = input().split()

temp = deque(string)
rez = []
while True:
    for _ in range(len(temp)):
        if temp[0].isdigit():
            print(int(temp[0]))
        x = temp.popleft()
        if x[-1] != "-" and len(x) > 1 or x.isdigit():
            rez.append(int(x))
        else:
            result = evaluator(rez, x)
            break

    if len(temp) == 0:
        break
    temp.appendleft(str(result))
    rez = []
print(result)
