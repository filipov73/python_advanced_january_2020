from collections import deque

add_num, del_num, search_num = list(map(int, input().split(" ")))
d = deque(list(map(int, input().split(" "))))


for _ in range(del_num):
    d.popleft()
if len(d) == 0:
    print(0)
elif search_num in d:
    print("True")
else:
    print(min(d))
