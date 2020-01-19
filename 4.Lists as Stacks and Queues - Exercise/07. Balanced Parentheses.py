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

#
# parentheses = input()
# stack = []
# pairs = {
#     "{": "}",
#     "[": "]",
#     "(": ")"
# }
# valid = True
#
# for el in parentheses:
#     if el in "{[(":
#         stack.append(el)
#     elif el in ")]}":
#         if stack:
#             current = stack[-1]
#             if pairs[current] == el:
#                 stack.pop()
#             else:
#                 valid = False
#                 break
#         else:
#             valid = False
#             break
# if valid:
#     print("YES")
# else:
#     print("NO")
