clothes = [int(x) for x in input().split(" ")]
capacity = int(input())
box = 0
cl = 0
temp_capacity = 0
while clothes:
    cl = clothes.pop()
    temp_capacity += cl
    if temp_capacity > capacity:
        temp_capacity = 0
        box += 1
        clothes.append(cl)
    elif temp_capacity == capacity:
        temp_capacity = 0
        box += 1
        if not clothes:
            break
    if not clothes:
        box += 1
        break
print(box)
