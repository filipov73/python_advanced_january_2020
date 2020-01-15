string = input()

bracket_idx_stack = []

for idx in range(len(string)):
    if string[idx] == "(":
        bracket_idx_stack.append(idx)
    elif string[idx] == ")":
        print(string[bracket_idx_stack.pop():idx+1])
