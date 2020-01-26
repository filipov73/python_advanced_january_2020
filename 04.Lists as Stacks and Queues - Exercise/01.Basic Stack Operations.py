operations = list(map(int, input().split(" ")))
stack = list(map(int, input().split(" ")))
n, s, x = operations

for _ in range(s):
    stack.pop()
if x in stack:
    print(f"True")
else:
    if len(stack) == 0:
        print(f"0")
    else:
        print(min(stack))

