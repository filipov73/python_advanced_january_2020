
string = input()

new_list = []

if len(string) % 2 != 0:
    print("NO")
else:

    for ch in string:
        if ch == "{":
            new_list.append(1)
        elif ch == "[":
            new_list.append(2)
        elif ch == "(":
            new_list.append(3)
        elif ch == "}":
            if new_list[-1] == 1:
                new_list.pop()
            else:
                print("NO")
                break
        elif ch == "]":
            if new_list[-1] == 2:
                new_list.pop()
            else:
                print("NO")
                break
        elif ch == ")":
            if new_list[-1] == 3:
                new_list.pop()
            else:
                print("NO")
                break
    if not new_list:
        print("YES")

# from collections import deque
# new_list = deque([])
# parenthesis = {
#     "{": 1,
#     "[": 2,
#     "(": 3,
#     ")": 13,
#     "]": 12,
#     "}": 11,
#     " ": 0
# }
# for ch in string:
#     new_list.append(parenthesis[ch])

# if len(new_list) % 2 != 0:
#     print("NO")
# else:
#     while new_list:
#         first = new_list.popleft()
#         last = new_list.pop()
#         if first != last - 10:
#             print("NO")
#             break
#         else:
#             if not new_list:
#                 print("YES")
#                 break
#
#
