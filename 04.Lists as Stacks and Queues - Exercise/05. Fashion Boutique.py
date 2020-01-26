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



# clothes = [int(x) for x in input().split()]
# rack = int(input())
# rack_count = 0
# total = 0
#
# while clothes:
#     current = clothes[-1]
#     if rack >= total + current:
#         total += clothes.pop()
#     else:
#         total = 0
#         rack_count += 1
# if total > 0:
#     rack_count += 1
# print(rack_count)
