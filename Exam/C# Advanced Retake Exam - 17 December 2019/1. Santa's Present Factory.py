from collections import deque

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

ready_toys = {}
target = None
materials_box = [int(x) for x in input().split(" ")]
magic_box = deque([int(x) for x in input().split(" ")])

while True:
    if len(materials_box) == 0 or len(magic_box) == 0:
        break
    material = materials_box.pop()
    magic = magic_box.popleft()
    if material == 0 or magic == 0:
        if material != 0:
            materials_box.append(material)
        if magic != 0:
            magic_box.appendleft(magic)
        continue
    present = magic * material
    if present > 0:
        for key, value in presents.items():
            if present == value:
                if key not in ready_toys:
                    ready_toys[key] = 0
                ready_toys[key] += 1
                target = True
                break
        if not target:
            materials_box.append(material + 15)
        target = False
    elif present < 0:
        materials_box.append(magic + material)

if ("Doll" in ready_toys.keys() and "Wooden train" in ready_toys.keys()) or ("Teddy bear" in ready_toys.keys() and "Bicycle" in ready_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_box:
    print(f"Materials left: {', '.join(map(str, reversed(materials_box)))}")
if magic_box:
    print(f"Magic left: {', '.join(map(str, magic_box))}")
ready_toys_sorted = sorted(ready_toys.items())
for toy, value in ready_toys_sorted:
    print(f"{toy}: {value}")
#
# from collections import deque
#
# presents = {
#     "Doll": 150,
#     "Wooden train": 250,
#     "Teddy bear": 300,
#     "Bicycle": 400,
# }
#
# ready_toys = {}
#
# materials_box = [int(x) for x in input().split()]
# magic_box = deque([int(x) for x in input().split()])
#
# while True:
#     if len(materials_box) == 0 or len(magic_box) == 0:
#         break
#     material = materials_box.pop()
#     magic = magic_box.popleft()
#
#     present = magic * material
#
#     if present in presents.values():
#         for key, value in presents.items():
#             if present == value:
#                 if key not in ready_toys:
#                     ready_toys[key] = 0
#                 ready_toys[key] += 1
#                 break
#     else:
#
#         if present > 0:
#             materials_box.append(material + 15)
#
#         elif present < 0:
#             rez = material + magic
#             materials_box.append(rez)
#         else:
#             if material != 0:
#                 materials_box.append(material)
#             if magic != 0:
#                 magic_box.appendleft(magic)
#
# if ("Doll" in ready_toys.keys() and "Wooden train" in ready_toys.keys()) or ("Teddy bear" in ready_toys.keys() and "Bicycle" in ready_toys.keys()):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials_box:
#     print(f"Materials left: {', '.join(map(str, reversed(materials_box)))}")
# if magic_box:
#     print(f"Magic left: {', '.join(map(str, magic_box))}")
#
# for toy, value in sorted(ready_toys.items()):
#     print(f"{toy}: {value}")
#



#
# from collections import deque
#
# presents = {
#     "Doll": 150,
#     "Wooden train": 250,
#     "Teddy bear": 300,
#     "Bicycle": 400,
# }
#
#
# ready_toys = {
#     "Doll": 0,
#     "Wooden train": 0,
#     "Teddy bear": 0,
#     "Bicycle": 0,
# }
#
#
# materials_box = [int(x) for x in input().split()]
# magic_box = deque([int(x) for x in input().split()])
#
# while True:
#     if len(materials_box) == 0 or len(magic_box) == 0:
#         break
#     material = materials_box.pop()
#     magic = magic_box.popleft()
#
#     present = magic * material
#
#     if present in presents.values():
#         for key, value in presents.items():
#             if present == value:
#                 # if key not in ready_toys:
#                 #     ready_toys[key] = 0
#                 ready_toys[key] += 1
#     else:
#
#         if present > 0:
#             materials_box.append(material + 15)
#
#         elif present < 0:
#             rez = material + magic
#             materials_box.append(rez)
#         else:
#             if material != 0:
#                 materials_box.append(material)
#             if magic != 0:
#                 magic_box.appendleft(magic)
#
# success = (ready_toys["Doll"] and ready_toys["Wooden train"]) or (ready_toys["Teddy bear"] and ready_toys["Bicycle"])
# if success:
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials_box:
#     print(f"Materials left: {', '.join(map(str, reversed(materials_box)))}")
# if magic_box:
#     print(f"Magic left: {', '.join(map(str, magic_box))}")
#
# for toy, value in sorted(ready_toys.items()):
#     if value:
#         print(f"{toy}: {value}")
