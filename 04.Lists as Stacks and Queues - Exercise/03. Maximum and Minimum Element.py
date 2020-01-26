num = int(input())

s = []

for _ in range(num):
    operation = list(map(int, input().split(" ")))
    if operation[0] == 1:
        s.append(operation[1])
    elif s:
        if operation[0] == 2:
            s.pop()
        elif operation[0] == 3:
            print(max(s))
        elif operation[0] == 4:
            print(min(s))
res = [str(s.pop()) for _ in range(len(s))]
print(", ".join(res))

