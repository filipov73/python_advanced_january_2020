str_list = list(input())

res1 = [str_list.pop() for _ in range(len(str_list))]
print("".join(res1))


#######

string = input()


print(string[::-1])
